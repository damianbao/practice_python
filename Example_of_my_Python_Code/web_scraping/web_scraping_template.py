#each website is unique in its source code so this is not a cookie cutter
#scenario.
import webbrowser, requests, bs4

#webbrowser.open ("https://forecast.weather.gov/MapClick.php?lat=43.6592&lon=-70.2567#.W1eV5dJKjIU")
#access to the webpage

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=43.6592&lon=-70.2567#.W1eV5dJKjIU')
page_bs = bs4.BeautifulSoup(page.text, 'html.parser') #could save html source code to text file and use bs4 on that.

temp = page_bs.find(class_='myforecast-current-lrg')

print(temp)
print(temp.contents[0])
t = temp.contents[0]
print(t[:-2])


page2 = requests.get("http://physicsbuzz.physicscentral.com/")
page2_bs = bs4.BeautifulSoup(page2.text, 'html.parser') #could save html source code to text file and use bs4 on that.

collection = page2_bs.find(class_='date-outer')


titles = collection.find_all('a')

print(titles)
print()
cleantext = titles[1]
print(cleantext)

                    
                    
   


