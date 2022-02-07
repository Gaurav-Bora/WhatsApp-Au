import pywhatkit
import requests
import time
import datetime
import json
import schedule
def job():
    now = datetime.datetime.now()
    r = requests.get('http://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    a = json.loads(r.text)
    btc_str = '1 BItcoin will cost you' + str(a['bitcoin']['usd']) + 'US dollers.'
    pywhatkit.sendwhatmsg('+919****', btc_str,now.hour,now.minute+1)
job()
schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


