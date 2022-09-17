import requests
import json

url = "http://localhost:5000/image/create"

payload = json.dumps({
  "name": "dog_image_4",
  "link": "https://e3.365dm.com/22/05/768x432/skynews-pug-dog_5774995.jpg?20220518002633",
  "category": "dog"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
  