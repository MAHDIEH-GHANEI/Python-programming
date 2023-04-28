time=int(input())
hour=time//3600
r=time-3600*hour
minutes=r//60
Second=r-60*minutes
print(hour , ":" , minutes , ":" , Second)