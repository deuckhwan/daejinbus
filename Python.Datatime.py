import time, datetime, requests

resp = requests.get("https://api.bithumb.com/public/ticker/BTC")
print(f'{resp.content}')
now = datetime.datetime.now()
print(f'{now}\n{now + datetime.timedelta(hours=5, minutes=30)}')
print(f'{now}\n{now - datetime.timedelta(days=3)}')
nowtime = time.time()

print(f'{nowtime}')

local_time = time.localtime(time.time())
print(f'{local_time}')
