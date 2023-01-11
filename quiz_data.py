#API Data request

import requests

#set parametes for API Request
parameters = {
    "amount": 20,
    "type" : "boolean"
}
response = requests.get("https://opentdb.com/api.php?amount=20&category=9&difficulty=medium&type=boolean", params = parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
