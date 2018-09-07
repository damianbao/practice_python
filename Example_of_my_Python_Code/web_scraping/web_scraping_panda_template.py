
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from urllib.request import urlopen
from bs4 import BeautifulSoup





url = "http://physicsbuzz.physicscentral.com/"
html = urlopen(url)
soup = BeautifulSoup(html,  'html.parser')
type(soup)
text = soup.get_text()
titles = soup.find_all('a')
websites = []



for title in titles:
    
    src = (title.get("href"))
    print ()
    websites.append(src)
print (websites[:10])
    


