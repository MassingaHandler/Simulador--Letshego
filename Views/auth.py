import firebase
import pyrebase
import firebase_admin
import os
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
import pickle


# API = os.getenv("API")

cred = credentials.Certificate("letshego-simulador.json")
firebase_admin.initialize_app(cred)

firebaseConfig = {
  "apiKey": "AIzaSyDidoQxzVfE_SR_fLzva2kWIZrLjkL2lks",
  "authDomain": "letshego-simulador.firebaseapp.com",
  "projectId": "letshego-simulador",
  "storageBucket": "letshego-simulador.appspot.com",
  "messagingSenderId": "1089941649587",
  "appId": "1:1089941649587:web:b32e99ed74cb5625be98c6",
  "measurementId": "G-7MZE20HCXH",
  'databaseURL': "https://letshego-simulador-default-rtdb.firebaseio.com/"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()



# email = 'teste@gmail.com'
# password = 'teste@123'
# name = 'patricio'

# firebase_auth.create_user(
#     email=email,
#     password=password,
#     display_name=name
# )


def create_user(name, email, password):
    try:
        user = firebase_auth.create_user(
            email=email,
            password=password,
            display_name=name)
        return user.uid
    except:
        return None


def reset_password(email):
    try:
        auth.send_password_reset_email(email)
        return not None
    except:
        return None


def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user['idToken']
    except:
        return None


def store_session(token):
    if os.path.exists('token.pickle'):
        os.remove('token.pickle')
    with open('token.pickle', 'wb') as f:
        pickle.dump(token, f)


def load_token():
    try:
        with open('token.pickle', 'rb') as f:
            token = pickle.load(f)
        return token
    except:
        return None


def authenticate_token(token):
    try:
        result = firebase_auth.verify_id_token(token)

        return result['user_id']
    except:
        return None


def get_email(token):
    try:
        result = firebase_auth.verify_id_token(token)

        return result['email']
    except:
        return None


def revoke_token(token):
    result = firebase_auth.revoke_refresh_tokens(authenticate_token(token))
    if os.path.exists('token.pickle'):
        os.remove('token.pickle')