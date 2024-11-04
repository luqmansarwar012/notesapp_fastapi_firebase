from .constants import FIREBASE_DATABASE_URL, FIREBASE_CONFIG
from firebase_admin import credentials, initialize_app, auth, db
import pyrebase

cred = credentials.Certificate("./service_account_key.json")
firebase_admin_app = initialize_app(cred, {"databaseURL": FIREBASE_DATABASE_URL})

pyrebase_client_app = pyrebase.initialize_app(FIREBASE_CONFIG)


def get_database_reference():
    return db


def authenticate_user(email, password):
    return pyrebase_client_app.auth().sign_in_with_email_and_password(email, password)


def signup_user(user_info):
    user = pyrebase_client_app.auth().create_user_with_email_and_password(
        user_info.email, user_info.password
    )
    if not user:
        return None
    return user


def get_access_token(credentials):
    user = authenticate_user(credentials.email, credentials.password)
    token = user["idToken"]
    return token


def verify_token(token):
    user_info = auth.verify_id_token(token)
    return user_info
