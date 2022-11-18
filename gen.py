from __future__ import unicode_literals
from __future__ import print_function
from os.path import abspath, join, dirname
import random
import webbrowser
import asyncio
import re
from selenium import webdriver
import string
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains


async def main():
    print('Hello ...')
    await asyncio.sleep(2)
    print('... World!')
    
async def main2():
    print('Hello ...')
    await asyncio.sleep(20)
    print('... World!')
    

full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'first:male': full_path('dist.male.first'),
    'first:female': full_path('dist.female.first'),
    'last': full_path('dist.all.last'),
}


def get_name(filename):
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name
    return ""  # Return empty string if file is empty


def get_first_name(gender=None):
    if gender not in ('male', 'female'):
        gender = random.choice(('male', 'female'))
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return "{0} {1}".format(get_first_name(gender), get_last_name())





web = webdriver.Chrome()
url = input("Enter the url")
web.get(url)

asyncio.run(main())

firstname = get_first_name()
fn = web.find_element_by_id("FirstName")
for char in firstname:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       fn.send_keys(char)

lastname = get_last_name()
ln = web.find_element_by_id("LastName")
for char in lastname:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       ln.send_keys(char)

email = firstname+lastname+str(random.randint(1, 100))+"@yahgmail.com"
mail = web.find_element_by_id("Email")
for char in email:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       mail.send_keys(char)


pass_length = random.randint(15, 18)
characters = string.ascii_letters + string.digits + string.punctuation
pw = "".join(random.choice(characters) for i in range(pass_length))
passw = web.find_element_by_id("CreatePassword")
for char in pw:
       start = 0.4 #please edit the speed here
       stop = 0.6 #change this (the maximum value is 1 or 0.9)
       step = 0.3
       precision = 0.1
       f = 1 / precision
       n = random.randrange(start * f, stop * f, step * f) / f
       time.sleep(n)
       passw.send_keys(char)
       
asyncio.run(main())
try:
    web.find_element_by_id("account-create-check").click()
except:
    pass
web.find_element_by_xpath('//*[@id="create_customer"]').click()

print(email+":"+pw+":"+firstname+":"+lastname)

