import requests
import configparser
from payLoad import *
from utilities.resources import *
from utilities.Configurations import *

config=getConfig()
url=getConfig()['API']['endpoint']+ApiResources.addBook
headers={"Content-Type": "application/json"}
query='select * from CustomerInfo'
addBook_response = requests.post(url,
                                 json=buildPayLoadFromDB(query),
                                 headers=headers, )

print(addBook_response.json())
respone_json = addBook_response.json()
print(type(respone_json))

bookId = respone_json['ID']
print(bookId)
# Delete Book
deleteurl=url=getConfig()['API']['endpoint']+ApiResources.deleteBook

response_deleteBook = requests.post(deleteurl, json={

    "ID": bookId
}, headers=headers,
                                     )

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"
