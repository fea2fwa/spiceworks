def questionerpostnum(file="dellhw-questioner.txt"):
   questioners={}
   with open(file, encoding='utf-8') as f:
       for row in f:
           rep = row.rstrip()
           if rep in questioners.keys():
               questioners[rep] += 1
           else:
               questioners[rep] = 1

   questionerstats_output=open("dellhw-questioner-stats.txt", "w+", encoding="UTF-8")
   
   for i,v in questioners.items():
       questionerstats_output.write(i+","+str(v)+"\n")

   questionerstats_output.close()

def replierpostnum(file="dellhw-replier.txt"):
   repliers={}
   with open(file, encoding='utf-8') as f:
       for row in f:
           rep = row.rstrip()
           if rep in repliers.keys():
               repliers[rep] += 1
           else:
               repliers[rep] = 1

   replierstats_output=open("dellhw-replier-stats.txt", "w+", encoding="UTF-8")
   
   for i,v in repliers.items():
       replierstats_output.write(i+","+str(v)+"\n")

   replierstats_output.close()
