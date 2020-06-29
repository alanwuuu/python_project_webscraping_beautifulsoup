from bs4 import BeautifulSoup
import requests

import pandas as pd
import matplotlib.pyplot as plt


req = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')
soup = BeautifulSoup(req.content,'lxml')

#creating a list for all the chocolate ratings
coca_ratings_list = soup.find_all('td', class_='Rating')
rating=[]

for x in coca_ratings_list:
  try:
    rating.append(float(x.text))
  except:
    not_append = x.text          #getting rid of the first element, which is the title
    
print(rating[:10])

#ploting a basic histogram to get the distribution of ratings
plt.hist(rating)
plt.show()

#creating a list for all the companies
company_list = soup.find_all('td',class_='Company')
companies = []

for c in company_list:
    companies.append(c.text)
    
companies.pop(0)                #getting rid of the first element, which is the title
print(companies[:10])

#creating a data frame that contains the company and its rating
df = pd.DataFrame(
{'Company':companies, 'Rating':rating}, 
columns = ['Company','Rating'])

print(df)

#grouping the company and calculating its average rating
company_group = df.groupby('Company').Rating.mean().reset_index()
print(company_group)

#top 10 rated companies
top10_company = company_group.Rating.nlargest(10)
print(top10_company)    

#creating a list for all the chocolate percentages
coca_percentage_list = soup.find_all('td',class_='CocoaPercent')
coca_percentage = []
coca_percentage_list.pop(0)    #getting rid of the first element, which is the title

for p in coca_percentage_list:
    temp_p = float(p.text.split('%')[0])
    coca_percentage.append(temp_p)

print(coca_percentage) 

#adding the chocolate percentage list to the data fram
df['CocaPercentage'] = coca_percentage
print(df)

#plotting a scatter graph for each rating and its chocolate percentage
plt.clf()

plt.scatter(df.Rating,df.CocaPercentage)
plt.show()