g=open("input.txt").read()
w=141
p={*range(19739)}
r,d=[],set()
for x in p:
 c=o={x}
 if" ">g[x]or c<d:continue
 while o:={X for x in o for X in{x+1,x-1,x+w,x-w}&p if g[X]==g[x]}-c:c|=o
 d|=c;r+=c,
j=k=0
for u in r:a=len(u);exec("e=sorted(x for x in u if x+w not in u);s=1+sum(x+1!=X for x,X in zip(e,e[1:]));u={x//w+w*~(x%w)for x in u};j+=a*len(e);k+=a*s;"*4)
print(j,k)
