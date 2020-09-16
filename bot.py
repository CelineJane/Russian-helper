import tweepy
from bs4 import BeautifulSoup
import requests
import random

consumer_key = 'sgeGiNlqU32UkZh3BTw24jHJU'
consumer_secret = '6auSCDqUGzpy9GSESEQXrUY6Xv5qBgXBBgtth7YNpDPYwbcxhO'
access_token = '1036495179903946754-V7NSfDidEEPvFoASvGGzExWWTEDc70'
access_token_secret = 'Tp2KmXhIb0IpeVILFKy61cghREzw3kSBomiIvogakVNhc'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

from bs4 import BeautifulSoup
import requests
import random

page1 = requests.get('http://www.newworldencyclopedia.org/entry/Reptile')
page2 = requests.get('https://www.britannica.com/animal/lizard')
page3 = requests.get('http://www.reptileknowledge.com/articles/article19.php')
page4 = requests.get('https://www.britannica.com/animal/lizard/Form-and-function')

page_content1 = BeautifulSoup(page1.content, "html.parser")
page_content2 = BeautifulSoup(page2.content, "html.parser")
page_content3 = BeautifulSoup(page3.content, "html.parser")
page_content4 = BeautifulSoup(page4.content, "html.parser")

words1 = []

for p in page_content1.select('p'):
    words1.append(p.text.split())
    
for p in page_content2.select('p'):
    words1.append(p.text.split())
    
for p in page_content3.select('p'):
    words1.append(p.text.split())
    
for p in page_content4.select('p'):
    words1.append(p.text.split())

sentence =''

for i in range(3):

    rand1 = random.randint(0,len(words1)-7)
    
    rand2 = random.randint(0,len(words1[rand1])-1)
    
    
    nextWord = words1[rand1][rand2]
    
    while i == 0 and nextWord[0].islower():
        rand1 = random.randint(0,len(words1)-7)
        rand2 = random.randint(0,len(words1[rand1])-1)
        nextWord = words1[rand1][rand2]
      
    if i == 2:
        for n in range(1,30):
        
            sentence = sentence + nextWord + ' '
        
            if (rand2 + n) >= len(words1[rand1]):
                break
            else:
                nextWord = words1[rand1][rand2+n]
                if '.' in nextWord:
                    sentence = sentence + nextWord + ' '
                    break
    
    else:
        for n in range(1,30):
            
            sentence = sentence + nextWord + ' '
            
            if (rand2 + n) >= len(words1[rand1]):
                break
            elif '.' in nextWord:
                break
            elif 'and' in nextWord or 'if' in nextWord or 'so' in nextWord:
                rand1 = random.randint(0,len(words1)-7)
                rand2 = random.randint(0,len(words1[rand1])-1)
                nextWord = words1[rand1][rand2]
            #elif ',' in nextWord:
                #rand1 = random.randint(0,len(words1)-7)
                #rand2 = random.randint(0,len(words1[rand1])-1)
                #nextWord = words1[rand1][rand2]
                #while ',' not in words1[rand1][rand2-1]:
                    #rand1 = random.randint(0,len(words1)-7)
                    #rand2 = random.randint(0,len(words1[rand1])-1)
                    #nextWord = words1[rand1][rand2]
            else:
                nextWord = words1[rand1][rand2+n]
                
        
                

api.update_status(sentence)

    
