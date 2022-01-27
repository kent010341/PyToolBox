import requests

def __send_request(url, headers, body, method):
    return method(url, data=body, headers=headers)

def get(url, headers=None, body=None):
    __send_request(url, headers, body, method=requests.get)

def put(url, headers=None, body=None):
    __send_request(url, headers, body, method=requests.put)

def post(url, headers=None, body=None):
    __send_request(url, headers, body, method=requests.post)

def delete(url, headers=None, body=None):
    __send_request(url, headers, body, method=requests.delete)
