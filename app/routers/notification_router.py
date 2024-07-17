# from fastapi import APIRouter
# from app.services.notification_service import process_notification
#
# router = APIRouter()
#
#
# @router.post("/notifications/")
# async def create_notification(notification_data: dict):
#     # Call the business logic to process the notification
#     notification_id = await process_notification(notification_data)
#     return {"notification_id": notification_id}
#
# # Additional routes for notifications can be added here.
