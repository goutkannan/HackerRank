import sys


n,k = 100000,0
#n,k = [int(n),int(k)]
#rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [4187,5068]

rRObstacle = -1
cRObstacle = -1
rBRObstacle = -1
cBRObstacle = -1
rBObstacle = -1
cBObstacle = -1
rBLObstacle = -1
cBLObstacle = -1
rLObstacle = -1
cLObstacle = -1
rTLObstacle = -1
cTLObstacle = -1
rTObstacle = -1
cTObstacle = -1
rTRObstacle = -1
cTRObstacle = -1
count = 0


for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
   

  
  
    if((cObstacle < cRObstacle or rRObstacle == -1) and cObstacle > cQueen and rObstacle == rQueen):
      rRObstacle = rObstacle
      cRObstacle = cObstacle

    if(rQueen - rObstacle == cObstacle - cQueen and cObstacle > cQueen and rObstacle < rQueen  and ((rObstacle > rBRObstacle and cObstacle < cBRObstacle) or rBRObstacle == -1)):
      rBRObstacle = rObstacle
      cBRObstacle = cObstacle

    if((rObstacle > rBObstacle or rBObstacle == -1) and rObstacle < rQueen and cObstacle == cQueen):
      rBObstacle = rObstacle
      cBObstacle = cObstacle
  
    if(rQueen - rObstacle == cQueen - cObstacle and cObstacle < cQueen and rObstacle < rQueen and ((rObstacle > rBLObstacle and cObstacle > cBLObstacle) or rBLObstacle == -1)):
      rBLObstacle = rObstacle
      cBLObstacle = cObstacle 
    
    if((cObstacle > cLObstacle or rLObstacle == -1) and cObstacle < cQueen and rObstacle == rQueen):
      rLObstacle = rObstacle
      cLObstacle = cObstacle
    
    if(cQueen - cObstacle == rObstacle - rQueen and cObstacle < cQueen and rObstacle > rQueen and ((rObstacle < rTLObstacle and cObstacle > cTLObstacle) or rTLObstacle == -1)):
      rTLObstacle = rObstacle
      cTLObstacle = cObstacle

    if((rObstacle < rTObstacle or rTObstacle == -1) and rObstacle > rQueen and cObstacle == cQueen):
      rTObstacle = rObstacle
      cTObstacle = cObstacle

    if(rObstacle - rQueen == cObstacle - cQueen and cObstacle > cQueen and rObstacle > rQueen and ((rObstacle < rTRObstacle and cObstacle < cTRObstacle) or rTRObstacle == -1)):
      rTRObstacle = rObstacle
      cTRObstacle = cObstacle


count += (cRObstacle - cQueen -1) if (cRObstacle != -1)  else  (n - cQueen)
count += (rQueen - rBObstacle - 1) if (rBObstacle != -1)  else (rQueen - 1)
count += (cQueen - cLObstacle -1) if (cLObstacle != -1) else (cQueen - 1)
count +=  (rTObstacle - rQueen - 1) if (rTObstacle != -1) else (n - rQueen)

count += (cBRObstacle - cQueen -1) if (cBRObstacle != -1) else min(n - cQueen, rQueen - 1)
count += (cQueen - cBLObstacle - 1) if (rBLObstacle != -1) else min(cQueen - 1, rQueen - 1)
count += (cQueen - cTLObstacle -1) if (cTLObstacle != -1) else min(cQueen - 1, n - rQueen) 
count += (cTRObstacle - cQueen - 1) if (rTRObstacle != -1) else min(n - cQueen, n - rQueen)

print(count)