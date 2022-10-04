import requests_fun

r = requests_fun.delete('https://lptblc8mzk.execute-api.us-east-1.amazonaws.com/user-lists/test-user-list-2021-08-20T19-14-13/users/next')

print(r.json())