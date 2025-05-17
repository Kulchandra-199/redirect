from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

API_KEY = "kJ4ZlkzM"
CLIENT_CODE = "YOUR_TRADING_ID"  # e.g. D12345
CLIENT_SECRET = "a6444bb4-70d5-4302-8811-c64da81ed4b4"
REDIRECT_URI = "https://redirect-y481.onrender.com/callback"

@app.get("/callback")
async def callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        return {"error": "No auth code received"}

    payload = {
        # "client_code": CLIENT_CODE,
        "code": code,
        "grant_type": "authorization_code",
        "client_id": API_KEY,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI
    }

    response = requests.post("https://apiconnect.angelbroking.com/rest/auth/token", json=payload)
    if response.status_code == 200:
        data = response.json()
        access_token = data.get("data", {}).get("access_token", "")
        return {
            "message": "Access token received successfully.",
            "access_token": access_token,
            "full_response": data
        }
    else:
        return {
            "error": "Failed to exchange code for access token",
            "details": response.text
        }
