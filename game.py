p1=(input())
c1=(input())
p2=(input())
c2=(input())
if(c1=='rock' and c2=='scissor')or(c1=='paper' and c2=='rock')or(c1=='scissor' and c2=='paper'):
    print(p1,"is winner")
elif(c1=='rock' and c2=='rock')or(c1=='paper' and c2=='paper')or(c1=='scissor' and c2=='scissor'):
    print("Match is draw")
else:
    print(p2,"is winner")