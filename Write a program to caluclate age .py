from datetime import date
def caluclateage(birthdate):
	days_in_year = 365
	age = int((date.today()-birthdate).days/days_in_year)
	return age
print(caluclateage(date(2001,12,3)),'years')