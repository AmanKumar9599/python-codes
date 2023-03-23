amount=int(input("Enter the amount:"))
amount-=100
twok=amount//2000
amount=amount-twok*2000
fiveh=amount//500
amount=amount-fiveh*500
twoh=amount//200
amount=amount-twoh*200
oneh=amount//100
print("100 rupee notes:",oneh+1)
print("200 rupee notes:",twoh)
print("500 rupee notes:",fiveh)
print("2000 rupee notes:",twok)

