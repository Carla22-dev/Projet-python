from selenium  import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = 'https://www.thesun.co.uk/sport/football/'
#path = "C:/Users/cf974/ownloads/chromedriver-win64/chromedriver-win64" # introduce path here


#service = Service(executable_path=path)
#driver=webdriver.Chrome(service =service)
driver=webdriver.Chrome()
driver.get(website)
containers=driver.find_elements(by="xpath",value ='//div[@class="story__copy-container"]') #return a list

titles=[]
subtitles=[]
links=[]

for container in containers:
    title=container.find_element(by="xpath",value ='./a/h3').text
    subtitle=container.find_element(by="xpath",value ='./a/p').text
    link=container.find_element(by="xpath",value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


my_dict={'titles':titles, 'subtitle':subtitles, 'link':links}
df_headlines=pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv')


driver.quit()

c=input("digite uma letra")
print("Press enter to cose...")