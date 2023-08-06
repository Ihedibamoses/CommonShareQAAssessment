
## 1A. Test to check the web page is active or not
# import module
import requests
import urllib.request
 
# create a function for the check
# then pass the url
def url_ok(url):
     
    # exception block
    try:
       
        # pass the url into
        # request.hear
        response = requests.head(url)
         
        # check the status code
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError as e:
        return e
 
# driven code to be parsed
url = "https://www.myweb.com/"
url_ok(url)

# Get the webpage contents
page = urllib.request.urlopen('http://www.myweb.com')
print(page.read())




## 1B. Test to check the api link is active ands accessible or not

# import module
import requests
 
# create a function for the check
# then pass the url
def url_ok(api-url):
     
    # exception block
    try:
       
        # pass the url into
        # request.hear
        response = requests.head(api-url)
         
        # check the status code
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError as e:
        return e
 
# driven code to be parsed
api-url = "https://api.myweb.com"
url_ok(api-url)




##  2. Code to connect to the API endpoint to get the users list
import requests
import json
from terminaltables import AsciiTable

# Initiate the get method to initiate a HTTP GET request to the existing endpoint of the REST-based API and Print the status code
api_response = requests.get('https://api.myweb.com/api/v1/users')
print(api_response.status_code)

# retrieve the todo data which are provided by using the text property and parse the returned todo data into a JSON object which is stored in parse_json
data = api_response.text
parse_json = json.loads(data)
table = AsciiTable(parse_json, title='User Management Active users:')
table.justify = 'center'
table.inner_row_border = True
print(table.table)





## Bonus Track: Code considerations to be completed
class Browser:
def __init__(self, url: str):
# Url of the website
self.url = "www.myweb.com"
def find_object(self, "https://www.myweb.com": str):
# TODO: return the specified object of the website DOM

class API:
def __init__(self, url: str):
# Url of the website
self.url = "api.myweb.com"
def request(self, get:str, "https://api.myweb.com/api/v1/users":str)
# TODO: return the HTTP RESTful API response