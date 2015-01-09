v, e = map(int,raw_input().split() )
edgelist =[]
for edge in range(e):
    edgelist.append(list(map(int,raw_input().split() )))
print edgelist
child_list={}
for x in xrange(1,v+1):
    for i in edgelist:
        if x in i:
            i.remove(x)
            child_list[x] = child_list.get(x, [])+ i
for ver in child_list.keys():

print child_list