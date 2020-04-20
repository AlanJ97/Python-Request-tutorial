import requests

# Link of data in general
#r = requests.get('https://xkcd.com/353/')
# Link of image
#r = requests.get('https://imgs.xkcd.com/comics/python.png')
# Link to set parameters in URL
# payload = {'page':2, 'count':25}
# r = requests.get('https://httpbin.org/get', params=payload)
# Link for adding data to headers
# payload = {'username':'corey', 'password':'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)

r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth = ('corey', 'testing'))




# GET EVERYTHING


#print(r.text)

# GET IMAGE

'''
with open('comic.png','wb') as f:
    f.write(r.content)
print()
'''

# GET STATUS CODE
'''
print (r.status_code)
print (r.ok)
print (r.headers)
'''

# GET URL AND DATA RELATIONED

'''
print (r.text)
print (r.url)
'''
# GET DATA IN JSON

# r_dict = r.json()
# print(r_dict['form']['password'])

print (r)