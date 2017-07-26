import re

def makedict(line):
    result={} 
    line = line.replace(" = ","=")
    for l in line.split():
        
        key,value = l.split("=")
        result[key] = value

    return result 

lines = ["<tag1 name = \"some\" value = \"thing\">","<tag2 name = \"Name1\">","</tag2>","</tag1>"]

hrml={} 
tag=""
stack=[]
attrib={}
for l in lines:
    m =  re.match("<(\w+)\s*(.*)>",l)
    m1 = re.match("</(\w+)>",l)
    if m: 
    
        tag = m.group(1)
        rest = m.group(2)

        attrib = makedict(rest)
        hrml[tag] = attrib
        if len(stack)>0:
            hrml[stack[-1]]['child'] = tag 
        stack.append(tag) 
    
    elif m1:
        stack.remove(m1.group(1)) 

        #pop tag from stack 

print(hrml)

def decode(query):
    tags = re.split("\W",query)
    

    attrib = tags.pop()
    print(tags)
    print(attrib)

    flag=0
    for i in range(len(tags)):
        if tags[i] in hrml.keys():
            if i>0:
                if hrml[tags[i-1]]['child']==tags[i]:
                    continue
                else:
                    flag= -1
        else:
            
            flag= -1
    
    if(flag!=-1 and attrib in hrml[tags[-1]]   ):
        print(hrml[tags[-1]][attrib])
    else:
        print("Not Found!")




query = ["tag1.tag2~name","tag1~nam","tag3~value"] 
for q in query:
    decode(q)




decode("tag1.tag2~name")


