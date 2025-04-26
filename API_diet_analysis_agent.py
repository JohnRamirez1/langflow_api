
# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
from dotenv import load_dotenv
import os
load_dotenv()

LANGFLOW_API_KEY=os.environ["LF_DIET_EVALUATION"]
# The complete API endpoint URL for this flow
url = f"https://api.langflow.astra.datastax.com/lf/d173a45f-a20f-4a7b-96b5-3508026c3056/api/v1/run/5361f640-940f-42d2-9539-79302a725d06"  

# Request payload configuration
payload = {
    "input_value": "eggs. chocolate, bread and meat",  # The input value to be processed by the flow
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
    