import requests
import base64

# Replace this with the actual path to your image file
image_path = 'C:\\Users\\DZUNG NGUYEN\\Documents\\flaskProject\\testing\\test.png'


with open(image_path, 'rb') as image_file:
    # Encode the image as base64
    base64_data = base64.b64encode(image_file.read()).decode('utf-8')

# API endpoint
url = 'http://127.0.0.1:5000/image'

# JSON payload
payload = {'image_data': base64_data}

# Send POST request
response = requests.post(url, json=payload)
# // convert response in base64 to image
with open('../result1.png', 'wb') as f:
    f.write(base64.b64decode(response.json()['image_data']))

# Print the response
print(response.status_code)
print(response.json())