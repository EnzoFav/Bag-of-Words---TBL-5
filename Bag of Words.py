# Enzo Favareto da Costa

import requests
import bs4
from bs4 import BeautifulSoup
sites = ["https://en.wikipedia.org/wiki/Natural_language_processing", "https://www.ibm.com/cloud/learn/natural-language-processing", "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP", "https://realpython.com/nltk-nlp-python/#:~:text=Natural%20language%20processing%20(NLP)%20is,and%20contains%20human-readable%20text.", "https://towardsdatascience.com/7-nlp-techniques-you-can-easily-implement-with-python-dc0ade1a53c2"]

bag = []

for site in sites:
  page = requests.get(site)
  soup = BeautifulSoup(page.content, 'html.parser')
  
  x = 0
  
  while x < 100:
    try:
      texto = (soup.find_all('title')[x].get_text())
      texto = texto.split(" ")
      bag.append(texto)
    except:
      y = "meh"
    x = x + 1
    try:
      texto = (soup.find_all('p')[x].get_text())
      texto = texto.split(" ")
      bag.append(texto)
    except:
      y = "meh"



print(bag)