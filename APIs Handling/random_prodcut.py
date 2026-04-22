import requests

url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"

response = requests.get(url)
data = response.json()

if data ["success"] in data in "data":
    product = data["data"]
    
