from urllib.request import urlopen
from bs4 import BeautifulSoup
import ast

questioner_output=open("dellhw-questioner.txt", "w+", encoding="UTF-8")
replier_output=open("dellhw-replier.txt", "w+", encoding="UTF-8")
text_output=open("dellhw-spiceworks.txt", "w+", encoding="UTF-8")

def getSWstats(threadId,obj):
#  html=urlopen("https://community.spiceworks.com/topic/"+str(threadId))
 bsObj=obj
 title=bsObj.title.get_text()
 title=title.strip("EMC Community Network - DECN")
 title=title.strip(": ")
 questioner=bsObj.find("a", {"class":"jiveTT-hover-user jive-username-link"})
 questioner=questioner.get_text()
 qpostedtime=bsObj.find("span", {"class":"j-post-author"})
 qpostedtime=qpostedtime.get_text()
 textlist=qpostedtime.split(" ")
 time=textlist[4].split(":")
 hour=time[0]
 minute=time[1]
 hour=int(hour)
 summertime=0
 if textlist[5].count("AM") and hour != 12:
  hour=hour+17-summertime
 else:
  hour=hour+5-summertime
 if hour > 24:
  hour=hour-24-summertime
 print(title+"\n")
 output.write(title+"\n")
 csvoutput.write(str(threadId)+","+ title+","+questioner+","+str(hour)+":"+str(minute)+"\n")

def getThreadtitle(threadId,obj):
#  html=urlopen("https://community.spiceworks.com/topic/"+str(threadId))
 bsObj=obj
 bodylist=bsObj.findAll("script", {"data-gala-json":"galaTopicData"})
 for body in bodylist:
    text=body.get_text()
    title=text.split('subject":"')
    title=title[1].split('","root_post')
    print(title[0])
    text_output.write(title[0]+"\n")

def getParticipants(threadId,obj):
#  html=urlopen("https://community.spiceworks.com/topic/"+str(threadId))
 users=[]
 bsObj=obj
 bodylist=bsObj.findAll("a", {"user profile_link--user profile_link "})
 for body in bodylist:
    if body.get_text() != '':
      users.append(body.get_text())

 questioner=users[0]
 questioner_output.write(questioner+"\n")

 for i in range(len(users)):
    if users[i] != questioner:
       replier_output.write(users[i]+"\n")
        # repliers.append(users[i])
 


#  for i in range(len(repliers)):
#     replier_output.write(repliers[i]+"\n")

def getThreadquestion(threadId,obj):
#  html=urlopen("https://community.spiceworks.com/topic/"+str(threadId))
 bsObj=obj
 bodylist=bsObj.findAll("script", {"data-gala-json":"galaTopicData"})
 for body in bodylist:
    text=body.get_text()
    question=text.split('root_post":"')
    question=question[1].split('","tags')
    print(question[0])
    text_output.write(question[0]+"\n")


def getThreadreplies(threadId,obj):
#  html=urlopen("https://community.spiceworks.com/topic/"+str(threadId))
 bsObj=obj
 bodylist=bsObj.findAll("div", {"class":"post-body"})
 for body in bodylist:  
   print(body.get_text()+"\n")
   text_output.write(body.get_text()+"\n")


# startId=input("Enter the first thread# which in Spiceworks forum site: ")
# endId=input("Enter the last thread# which in Spriceworks forum site: ")
# endId=int(endId)+1

startId=2304500
endId=2304700

for i in range(int(startId), int(endId)):
 try:
  htmltemp=urlopen("https://community.spiceworks.com/topic/"+str(i))
 except:
  print("Thread#"+str(i)+" has been deleted or is an invalid or private thread.")
 else:
  bsObjTemp=BeautifulSoup(htmltemp)
  templist=bsObjTemp.findAll("span",{"class":"topic-chip forum-chip"})
  templist=str(templist)
#   getEcnstats(i)
#   getThreadtext(i)
  if "/hardware/dell" in templist:
#    getEcnstats(i)
   getThreadtitle(i,bsObjTemp)
   getParticipants(i,bsObjTemp)
   getThreadquestion(i,bsObjTemp)
   getThreadreplies(i,bsObjTemp)
#   elif "communityID = '3093';" in templist:
#    getEcnstats(i)
#    getThreadtext(i)
#   elif "communityID = '3094';" in templist:
#    getEcnstats(i)
#    getThreadtext(i)
#   elif "communityID = '3095';" in templist:
#    getEcnstats(i)
#    getThreadtext(i)
#   elif "communityID = '3096';" in templist:
#    getEcnstats(i)
#    getThreadtext(i)


questioner_output.close()
replier_output.close()
text_output.close()
