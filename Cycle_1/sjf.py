"""Write a program to implement SJF scheduling with arrival time(Non pre-emptive)"""

process=[]
n=int(input("Enter no of process: "))
ct=[0]*n
tat=[]
wt=[]
for i in range(n):
	process.append([])
	process[i].append(int(input("Enter process id: ")))
	process[i].append(int(input("Enter arrival time: ")))
	process[i].append(int(input("Enter burst time: ")))
	print ('')

process.sort(key = lambda process:process[1])

for i in range(n):
	process[i].append(i)

ct[0]=process[0][1]+process[0][2]
process[0].append(1)
c=ct[0]
for i in range(n):
	p=list(filter(lambda pr:pr[1]<=c and len(pr)==4,process))
	if p!=[]:
		p.sort(key = lambda p:p[2])
		c+=p[0][2]
		index=p[0][3]
		ct[index]=c
		process[index].append(1)

for i in range(n):
	tat.append(ct[i]-process[i][1])
	wt.append(tat[i]-process[i][2])
awt=0
atat=0
print ('pid\t\tarrival\t\tburst\t\tcompletion\tturn-around\twaiting')
for i in range(n):
	atat += tat[i]
	awt += wt[i]
	print (process[i][0],'\t\t',process[i][1],'\t\t',process[i][2],'\t\t',ct[i],'\t\t',tat[i],'\t\t',wt[i])
print(f'Average waiting time: {awt/n}')
print(f'Average turn-around time: {atat/n}')