import urllib.request
import urllib.error
import re

def url_hunt(url):
    working_url = url
    stored_key = 0
    url_prefix = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

    while True:
        page = urllib.request.urlopen(working_url)
        
        page_string = page.read().decode()
        print(page_string + " is the text found at " + working_url)
        try:
            stored_key = re.search('(?<=nothing is )(\d+)', page_string).group()
        except AttributeError:
            stored_key = input("Input the new stored key to start from, or n to quit: ")
        if stored_key == 'n':
            break
        working_url = url_prefix + stored_key
            
