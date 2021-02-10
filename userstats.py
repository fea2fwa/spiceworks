def userpostnum(file="dellhw-replier.txt"):
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
