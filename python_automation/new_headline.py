from selenium  import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

website = 'https://www.thesun.co.uk/sport/football/'
path = r'C:/Users/cf974/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe' # introduce path here



## headless
options=Options()
options.headless=True
options.add_argument("--headless")

service = Service(executable_path=path)
driver=webdriver.Chrome(service =service,options=options)

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
df_headlines.to_csv('headline-headless.csv')


driver.quit()
