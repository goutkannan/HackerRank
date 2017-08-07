#T= int(input())
T=1
inp = "456"
factor=[5,4,2]
while(T>0):
    data = [int(x) for x in inp] 
    x,y,z = data
    x*=4
    y*=5
    z*=6
    value=0
    
    if x<101 and y<101 and z<101:
        for i in range(0,3):
            value+= x*pow(10,i)*factor[i]
            value+= y*pow(10,i)*factor[i]
            value+= z*pow(10,i)*factor[i]
            
    else:
        print("0")
        break 

    print(value)
    print( (pow(10,9)+7)%value)
    T-=1
