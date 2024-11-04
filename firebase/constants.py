from common.service import get_env_variable
import json

with open("firebase_webapp_config.json", "r") as config_file:
    FIREBASE_CONFIG = json.load(config_file)

FIREBASE_DATABASE_URL = get_env_variable("FIREBASE_DATABASE_URL")
