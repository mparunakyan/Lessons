totalsec = int(input("Please input total seconds: "))
hours = totalsec//3600
minutes = (totalsec%3600)//60
seconds = (totalsec%3600)%60

if hours < 10 :
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10 :
    seconds = "0" + str(seconds)
#print("hour", hours)
#print("minutes", minutes)
#print("seconds", seconds)
print(f"{hours}:{minutes}:{seconds}")