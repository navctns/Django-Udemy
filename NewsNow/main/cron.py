
#crontab recurring function

from blacklist.models import BlackList

def my_job():
    b= BlackList(ip = "753669")
    b.save()