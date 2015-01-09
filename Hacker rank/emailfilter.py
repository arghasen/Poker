import re
count = int(raw_input())
emails =[]
for i in range(count):
    emails.append(raw_input())
print sorted(filter(lambda x:re.match(r'^[\w\d_-]+@[A-Za-z\d\d]+\.[\w]{1,3}$',x)!=None,emails))