"""import requests
import validators
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def IsItDown():
  print("Welcome to IsItDown.py!")
  print("Please write a URLs you want to check. (separated by comma)")
  URL_lst = list(map(str, input().split(',')))
  params = {'key':'value'}
  print(URL_lst)

  for i in range(len(URL_lst)):
    URL = URL_lst[i].strip()
    valid = validators.url(URL)
    
    if valid == False: #check URL is valid or not
        print(f"{URL} is not a valid URL")
        continue

    if 'http' not in URL:
        URL = 'http://' + URL
    
    try:
        request = requests.get(URL, params=params, timeout=5)
        print(f'{URL} is up!')
    except:
        print(f'{URL} is down!')
    

  print("Do you want to start over? y/n", end='\n')
  start_over = input()
  if start_over =='y' or  start_over == 'Y':
    clearConsole()
    IsItDown()
  elif start_over =='n' or start_over == 'N':
    print('bye!')
  else:
    print('wrong Command!')

IsItDown()
"""


import math

print(math.ceil(2.0))
print(10/3)