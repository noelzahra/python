# Using datettime library

from datetime import datetime, date, timedelta

now = datetime.now()
year = datetime.now().year
month = datetime.now().month
print(f"timestamp: {now}, Get year: {year}, Get month: {month}")

formatted_time = now.strftime("Today: %A date:%d/%m/%Y time: %H:%M:%S")
print(f"Formatted time: {formatted_time}")

daybatch = {
     'Log Id': '707022',
     'Log date': '5/14/20267:44:57 AM',
     'Instrument': 'ICTHouseholds2026',
     'Key': '',
     'Interviewer': 'ICTSup1',
     'Action': 'Create daybatch',
     'Success': 'Yes',
     'Message': "End creating daybatch for 5/14/2026. Number of included/processed records: 1230/2460. 1185 cases were excluded with reason: 'CaseCompleted'. 39 cases were excluded with reason: 'WrongDay'. 6 cases were excluded with reason: 'NumberOfCalls'. Cati Server Time Zone: W. Europe Standard Time (offset 01:00:00). DoNotCallBefore: 421, DoNotCallAfter: 1261. Found 1 TimeZones: CET (W. Europe Standard Time). Cases found: 2460: added 0 new records to Case Info, updated 2460 existing records in Case Info. TimeZone CET: DoNotCallBefore is 5/14/2026 7:00:00 AM (DayOffset: 0). DoNotCallAfter is 5/14/2026 9:00:00 PM (DayOffset: 0)."
    }

def get_log_date(daybatch):
    for item in daybatch:
        if item == 'Log date':
            #regex string to date
            log_date = datetime.strptime(daybatch[item], '%m/%d/%Y%I:%M:%S %p')

            #format date to string
            log_date_formatted = log_date.strftime('%d-%m-%Y %H:%M:%S %p') 
            return log_date_formatted

print(f"Log date: {get_log_date(daybatch)}")
print(daybatch['Message'].split('. ')[2])

# timedelta

today = date.today()
tdelta = timedelta(days=10)
print(f"Today: {today}, 10 days later: {today + tdelta}, 10 days ago: {today - tdelta}")

birthday = date(2026, 12, 21)
till_next_birthday = birthday - today
print(f"Days until next birthday: {till_next_birthday.days}")   
