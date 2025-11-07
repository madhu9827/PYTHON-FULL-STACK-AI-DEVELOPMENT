import requests
resp_data=requests.get('')
users=resp_data.json()
code=resp_data.status_code()
