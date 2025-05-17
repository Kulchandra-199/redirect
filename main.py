from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/callback", response_class=HTMLResponse)
async def callback(request: Request):
    code = request.query_params.get("code")
    return f"""
    <h2>Authorization Code Received</h2>
    <p><b>Code:</b> {code}</p>
    <p>Use this code to generate the access token using SmartAPI SDK.</p>
    """
