#Kristian McMahon
#Influencer
import pandas as pd
data=pd.read_csv('influencer.csv')
print(data)

#Init
month=data["Month"].tolist()
views=data["Views"].tolist()
dislikes=data["Dislikes"].tolist()
subscriber=data["Subscriber(+-)"].tolist()
revenue=data["Revenue"].tolist()
filter=[]

#Functions
#Challenge 1
def viewers(amount):
    for i in range(len(views)):
        if views[i]<=amount:
            filter.append([i])
    print(filter)
    filter.clear()

#Challenge 2
def subscribe(followers):
    for i in range(len(subscriber)):
        if subscriber[i]>=followers:
            filter.append([i])
    print(filter)
    filter.clear()

#Challenge 3
def scandal(moneyrev):
    for i in range(len(revenue)):
        if revenue[i]<=moneyrev:
            filter.append([i])
    print(filter)
    filter.clear()

viewers(2000)
print(data.loc[0 : 10])
subscribe(50000)
print(data.loc[64 : 72])
scandal(0)
print(data.loc[[98, 107]])
