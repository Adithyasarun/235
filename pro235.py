import requests

for i in range(1,500):
    url = f'http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}'
    res = requests.get(url=url)
    if res.status_code == 200:
        print(url)