import requests

def randorm_data_fetch():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    return data

#     if data["success"] and "data" in data:
#         user_data = data["data"]
#         username = user_data["login"]["username"]
#         country = user_data["location"]["country"]

#         return username,country
#     else:
#         raise Exception("filed to fetch data")
# def main():
#     try:
#         username, countary = randorm_data_fetch()
#         print(f"Username: {username} \n Country: {country}")
#     except Exception as e:
#         print(str(e))
# if __name__ == "__main":
#     main()

result = randorm_data_fetch()
print(result)
