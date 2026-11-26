#create post using requests
import requests
url="https://jsonplaceholder.typicode.com/posts"
payload= {
    "userId":1,
    "title":"My first post",
    "body":"This is the content of my first post"
}

response=requests.delete(url)
print("The status code is: ", response.status_code)
#print(response.json())

status_code=response.status_code

#if status_code==200:
    #print("The request was redirected")

#else:
    #print("The request was failed with status code: ", status_code)

assert status_code==200, "The request was failed with status code: {}".format(status_code)
print("The request was successful with status code: ", status_code)