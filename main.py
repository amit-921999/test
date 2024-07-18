from fastapi import FastAPI
# from app.routers import notification_router
# from firebase import initialize_firebase

app = FastAPI()

# Initialize Firebase Admin
# initialize_firebase()
#
# # Include routers
# app.include_router(notification_router.router)


@app.get("/")
def first_example():
    return {"GFG Example": "FastAPI"}


