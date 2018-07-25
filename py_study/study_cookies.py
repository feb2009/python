#import cookies
from http import cookies
import datetime
import random

expiration = datetime.datetime.now() + datetime.timedelta(days=30)
cookie = cookies.SimpleCookie()
cookie["session"] = random.randint(0, 1000000000)
cookie["session"]["domain"] = "localhost"
cookie["session"]["path"] = "/"
cookie["session"]["expires"] = \
expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")

print("Content-type: text/plain")
print(cookie.output(),"\n","Cookie set with: " + cookie.output())
