
# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
from dotenv import load_dotenv
import os
load_dotenv()

LANGFLOW_API_KEY=os.environ["LF_SOCIALMEDIA"]

# The complete API endpoint URL for this flow
url = f"https://api.langflow.astra.datastax.com/lf/d173a45f-a20f-4a7b-96b5-3508026c3056/api/v1/run/cbf12690-6e1c-4784-b049-0af3f1e04650"  

# Request payload configuration
payload = {
    "input_value": "Find the TikTok profile of the company OpenAI using Google search, then show me the profile bio and their latest video.",  # The input value to be processed by the flow
    "output_type": "chat",  # Specifies the expected output format
    "input_type": "chat"  # Specifies the input format
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {LANGFLOW_API_KEY}"  # Authentication key from environment variable'}
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
    