from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime as dt 

time_output=open("dellhw-posttime.txt", "w+", encoding="UTF-8")
questioner_output=open("dellhw-questioner.txt", "w+", encoding="UTF-8")
replier_output=open("dellhw-replier.txt", "w+", encoding="UTF-8")
text_output=open("dellhw-spiceworks.txt", "w+", encoding="UTF-8")

def getPosttime(threadId,obj):
   posttimes=[]
   bsObj=obj
   bodylist=bsObj.findAll("span", {"data-js-postprocess":"timestamp"})
   for body in bodylist:  
      posttimes.append(body.get_text())
 
   tmptime=posttimes[0]
   initpost=dt.strptime(tmptime, '%b %d, %Y at %H:%M UTC').strftime('%Y/%m/%d %H:%M')
   time_output.write(initpost+"\n")

def getThreadtitle(threadId,obj):
   bsObj=obj
   bodylist=bsObj.findAll("script", {"data-gala-json":"galaTopicData"})
   for body in bodylist:
      text=body.get_text()
      title=text.split('subject":"')
      title=title[1].split('","root_post')
      print(title[0])
      text_output.write(title[0]+"\n")

def getParticipants(threadId,obj):
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


def getThreadquestion(threadId,obj):
   bsObj=obj
   bodylist=bsObj.findAll("script", {"data-gala-json":"galaTopicData"})
   for body in bodylist:
      text=body.get_text()
      question=text.split('root_post":"')
      question=question[1].split('","tags')
      print(question[0])
      text_output.write(question[0]+"\n")


def getThreadreplies(threadId,obj):
   bsObj=obj
   bodylist=bsObj.findAll("div", {"class":"post-body"})
   for body in bodylist:  
      print(body.get_text()+"\n")
      text_output.write(body.get_text()+"\n")


# startId=input("Enter the first thread# which in Spiceworks forum site: ")
# endId=input("Enter the last thread# which in Spriceworks forum site: ")
# endId=int(endId)+1

startId=2304546
endId=2304820

for i in range(int(startId), int(endId)):
   try:
      htmltemp=urlopen("https://community.spiceworks.com/topic/"+str(i))
   except:
      print("Thread#"+str(i)+" has been deleted or is an invalid or private thread.")
   else:
      bsObjTemp=BeautifulSoup(htmltemp)
      templist=bsObjTemp.findAll("span",{"class":"topic-chip forum-chip"})
      templist=str(templist)

   if "/hardware/dell" in templist:
      getPosttime(i,bsObjTemp)
      getThreadtitle(i,bsObjTemp)
      getParticipants(i,bsObjTemp)
      getThreadquestion(i,bsObjTemp)
      getThreadreplies(i,bsObjTemp)

# questioner_output.close()
# replier_output.close()
# text_output.close()
