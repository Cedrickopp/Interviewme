# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
from google.cloud import secretmanager
import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()
initialize_app()

def access_secret_version(project_id: str, secret_id: str, version_id: str = "latest") -> str:
    """Access the secret version."""
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

@https_fn.on_request()
def test_openai_connection(req: https_fn.Request) -> https_fn.Response:
    try:
        project_id = os.getenv("PROJECT_ID")
        secret_id = os.getenv("SECRET_ID")
        if not project_id or not secret_id:
            raise ValueError("PROJECT_ID and SECRET_ID must be set in environment variables or .env file.")
        
        # Get the API key from Secret Manager
        api_key = access_secret_version(project_id, secret_id)
        
        # Configure OpenAI with the API key
        openai.api_key = api_key
        
        # Make a simple test call to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'Hello! This is a test message.'"}
            ]
        )
        
        # Return the response
        return https_fn.Response(
            json.dumps({
                "status": "success",
                "message": response.choices[0].message.content
            }),
            headers={"Content-Type": "application/json"}
        )
        
    except Exception as e:
        return https_fn.Response(
            json.dumps({
                "status": "error",
                "message": str(e)
            }),
            status=500,
            headers={"Content-Type": "application/json"}
        )

# Add your functions here