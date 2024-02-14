# doodstream
# for gogoanime
import requests
import re
import cloudscraper
import time
import random
import string

dood_url = "https://dood.wf/e/qwheic5v33ib"
print("Extracting : ",dood_url)

scraper = cloudscraper.create_scraper()
resp = scraper.get(dood_url)

# md5 pass key
pattern = r"\/pass_md5\/[\w-]+\/[\w-]+"
match = re.search(pattern, resp.text)
if match:
    _pass = match.group()
    print("Pass Extracted",_pass)
else:
    print("Pass extraction Error")

# doodstream for gogo need Referer header.
headers = {
    "Referer": dood_url,
}

# Token
pattern = r'return a \+ "(\?token=[^"]+&expiry=)"'
match = re.search(pattern, resp.text)
resp = scraper.get("https://dood.wf"+_pass,headers=headers)


# Make random hash and combine
if match:
    extracted_base = match.group(1)
    print("Extracted url:", resp.text + ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + extracted_base + str(int(time.time() * 1000)))
else:
    print("Url extraction failed.")
