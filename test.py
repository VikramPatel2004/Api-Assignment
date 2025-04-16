import requests

url = "http://127.0.0.1:8000/create-agent"

payload = {
    "platform": "vapi",
  
}

    


response = requests.get(url, json=payload)
print(response.status_code)
print(response.json())
   