from firebase_admin import credentials, initialize_app, messaging


def initialize_firebase():
    cred = credentials.Certificate({
        "type": "service_account",
        # Add other Firebase credentials here
    })
    initialize_app(cred)
