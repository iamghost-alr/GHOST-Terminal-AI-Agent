from datetime import datetime

def check_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def check_date():
    now = datetime.now()
    return now.strftime("%d %B %Y") 

def check_day():
    now = datetime.now()
    return now.strftime("%A")
