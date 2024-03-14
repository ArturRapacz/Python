import os, sys
import urllib.parse
import validators
import requests
from datetime import datetime


print("Number of arguments: ", len(sys.argv))
print("Arguments list: ", sys.argv)

url = "https://duckduckgo.com"

if len(sys.argv)>1:
    url = sys.argv[1]

print("Website to download: ", url)
scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

print("Current working directory:", os.getcwd())

if not os.path.exists("./websites"):
    os.mkdir("websites")

parsedUrl = urllib.parse.urlparse(url)
print(parsedUrl)

validFlag = validators.url(url)

if validFlag:
    print("URL:",url,"is valid")
else: 
    print("URL:",url,"is invalid")
    raise Exception("BAD URL!")

response = requests.get(url, allow_redirects=True)

if response.ok == True:
    print("Response ok from server for url:", url)
    now = datetime.now()
    dateString = now.strftime("%d.%m.%Y %H.%M.%S")
    print(dateString)
    fileName = "./websites/" + parsedUrl.netloc + " " + dateString + ".html"
    print(fileName)
    fh = open(fileName, "wb")
    fh.write((response.content))
    fh.close()

