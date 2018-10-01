#Importing Sentence analyser Libarary textblob
#Citation:http://textblob.readthedocs.io/en/dev/

#Importing counter library
from textblob import TextBlob
import sys
from collections import Counter

#Opening Data file in UTF8 encoding as facebook data is in UTF8 encoding
f=open ('othersComment.txt','r',encoding='UTF8')

#names:- A list containing name of people who interacted with the user
names=[]

#A loop to find name of all the people who interacted with the user
for line in f:
    a=line.split()
    names.append(a[0]+' '+a[1])

#finding frequency and name of the person who interacted the most with the user using counter library
blah = Counter(names).most_common(1)

#Using dataset in UTF8 format this dataset has comments of the user sorted according to time posted
z=open ('othersComment.txt','r',encoding='UTF8')

#sentim: A list containing sentiments of comments of the user
sentim=[]

#A loop to find sentiment of individual comment using Textblob library
for sen in z:
    analysis = TextBlob(sen)
    value=analysis.sentiment.polarity
    sentim.append(value)

#pre: previous sentiment, Cost: total of sentiment change, count: how many times sentiment has changed
pre=-1
cost=0
count=0

#A loop to find frequency of sentiment changes and total of change in sentiments weights are as follows
#most negative -> (-1 to -0.5)
#negative -> (-0.5 to 0.0)
#posetive -> (0.0 to 0.5)
#totaly posetive -> (0.5 to 1.0)

#cost of changes are as follows
#totally posetive to posetive and vice versa-> 10
#posetive to negative and vice versa -> 20
#negative to totaly negative and vice versa -> 30
#totally posetive to negative and vice versa -> 40
#posetive to totally negative and vice versa -> 50
#negative to posetive and vice versa -> 60

for it in sentim:
    curr=-1
    if(it<=-0.5):
        curr=1
    elif (it<=0):
        curr=2
    elif (it<=1.5):
        curr=3
    else:
        curr=4
        
    if(pre==-1):
        pre=curr
        continue
    
    if((curr==1 and pre==2) or (curr==2 and pre==1)):
        cost=cost+30
        count=count+1
    elif((curr==1 and pre==3) or (curr==3 and pre==1)):
        cost=cost+50
        count=count+1
    elif((curr==1 and pre==4) or (curr==4 and pre==1)):
        cost=cost+60
        count=count+1
    elif((curr==2 and pre==3) or (curr==3 and pre==2)):
        cost=cost+20
        count=count+1
    elif((curr==2 and pre==4) or (curr==4 and pre==2)):
        cost=cost+40
        count=count+1
    elif((curr==4 and pre==3) or (curr==3 and pre==4)):
        cost=cost+10
        count=count+1
    pre=curr

#we calculate average of changes as avgcost    
avgcost=cost/count

#Finding nature gradient of user as per avgcost
nature=-1
if(avgcost<=10):
    nature=1
elif(avgcost<=20):
    nature=2
elif(avgcost<=30):
    nature=3
elif(avgcost<=40):
    nature=4
elif(avgcost<=50):
    nature=5
elif(avgcost<=60):
    nature=6

#printing nature of user
if(nature==6):
    print("The Person is short tempered")
elif(nature==5):
    print("The Person is sensitive")
elif(nature==4):
    print("The Person is realistic and reserved")
elif(nature==3):
    print("The Person is logical")
elif(nature==2):
    print("The Person is cool but have a jugmental nature")
elif(nature==1):
    print("The person is calm like MS Dhoni")

#printing the name of person with whome the current person interacts most
print ("The Person Who Interact the most and frequency of interaction: "+str(blah))
