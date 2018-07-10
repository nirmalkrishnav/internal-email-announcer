import json
import datetime
from pprint import pprint

with open('data.json') as f:
    data = json.load(f)

now = datetime.datetime.now()


if now.month < 10 :
    month = '0' + str(now.month)
else :
    month= str(now.month)

if now.day < 10 :
    day = '0' + str(now.day)
else :
    day = str(now.day)  

date = month + '/' + day
pprint("today is :" + date)

collection = data['users'][date]

for index,item in enumerate(collection):
    pprint(item['emailID'])