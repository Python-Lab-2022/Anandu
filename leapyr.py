import datetime
today = datetime.date.today()
year = today.year
print("Current year is")
print(year)
val = int(input("Enter Limit Year: "))
for year in range(year,val):
    if year%4==0:
        print(year,"is a leap year")
    
