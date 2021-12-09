#function diffDate(x) untuk menghitung selisih hari

from datetime import*

def diffDate(x):
    now = datetime.date(datetime.now())
    nexttime = datetime.strptime(x, "%Y-%m-%d").date()
    time = (nexttime-now)
    print(time.days)

diffDate("2021-12-30")
