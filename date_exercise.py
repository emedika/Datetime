from datetime import date,timedelta

todayDate = date.today()
daysToSubtract = int(input("Enter the number of days to subtract from today: ") or "5")
pastDate = todayDate - timedelta(days=daysToSubtract)
print(pastDate)


