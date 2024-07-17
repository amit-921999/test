# import firebase_admin
# from firebase_admin import credentials, messaging
#
# # Initialize Firebase Admin SDK if not already initialized
# if not firebase_admin._apps:
#     cred = credentials.Certificate({
#         # Your Firebase project credentials
#     })
#     firebase_admin.initialize_app(cred)
#
# def send_firebase_message(token, title, body):
#     """
#     Sends a message to a specific device.
#
#     Args:
#     - token: The FCM token of the device to send the message to.
#     - title: The title of the notification.
#     - body: The body content of the notification.
#     """
#     message = messaging.Message(
#         notification=messaging.Notification(
#             title=title,
#             body=body,
#         ),
#         token=token,
#     )
#
#     # Send a message to the device corresponding to the provided token.
#     response = messaging.send(message)
#     return response