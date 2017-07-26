import sys

def isPalindrome(s):
      return True if s==s[::-1] else False

def richieRich(s, n, k):
    word = list(s)
    tracker  = [0]*n 
    flag=True
    
    for i in range(0,int(n/2)):
              
              if word[i] > word[n-i-1] and k>0:
                          word[n-i-1] = word[i]
        tracker[n-i-1] =1
        
        k-=1
      elif word[i] < word[n-i-1] and k>0:
                  word[i] = word[n-i-1]
        
        tracker[i] =1
        k-=1
      
    if(isPalindrome("".join(word))==False):
              return "-1"
    
    #maximize the value 
    
    for i in range(0,int(n/2)):
              if k==0:
                          break
      if(word[i]!="9"):
                  if (tracker[i]==1) or (tracker[n-i-1]==1):
                                word[i]="9"
          word[n-i-1]="9"
          k-=1
        elif k>=2:
                      word[i]="9"
          word[n-i-1]="9"
          k-=2
    
    if(n%2!=0 and k>0):
              word[int(n/2)] = "9"
  
    return "".join(word)


l = (input().strip().split())
n = int(l[0])
k = int(l[1])

s = input().strip()
result = richieRich(s, n, k)
print(result)


