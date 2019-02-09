#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 21:01:10 2019

@author: rr-coding
"""


'''
This script scrapes brexit headlines from websites

'''

# start

import requests
from bs4 import BeautifulSoup
import re

# read in objects

outputlist = []


'''
myurllist = ['https://www.bbc.co.uk/news', 
             'https://www.theguardian.com/uk',
             'https://www.dailymail.co.uk/home/index.html']
'''

source_dictionary = {
   '[BBC]' : 'https://www.bbc.co.uk/news', 
   '[Guardian]' : 'https://www.theguardian.com/uk',
   '[Mail]' : 'https://www.dailymail.co.uk/home/index.html'
}


mykeywordlist = ['Brexit', 'EU', 'Europe', 'brexit']

mytaglist = ['h2', 'h3', 'h4']

snippet_length = 60

for source in source_dictionary:

    url = source_dictionary.get(source)
    read_object = requests.get(url)
    read_html = read_object.text

    soup = BeautifulSoup(read_html,features="lxml")

# construct the output lines one by one
# for each keyword, for each tag, find each headline!
    
    
    for keyword in mykeywordlist:

        for tag in mytaglist:
            
            for i in soup.find_all(tag):
                if keyword in i.text:

                    if len(i.text)>snippet_length: 
                        spacer_text = '... ' 
                    else: 
                        spacer_text = ' '
                        
                    test_text = i.text[0:snippet_length] + spacer_text + source
 
# various operations to remove extraneous chars
                    
                    test_text = test_text.strip()
                    test_text = test_text.replace('\n', ' ').replace('\r', '')
                    test_text = re.sub(' +', ' ', test_text)

# only write to the list if not a duplicate
                    
                    if test_text not in outputlist: 

                        outputlist.append(test_text)

print('*******')

for i in range (0, len(outputlist)):
    print(outputlist[i])

print('*******')


# end
        
