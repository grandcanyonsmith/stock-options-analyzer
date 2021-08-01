import time
from datetime import datetime
from pytz import timezone
import requests

def vix_metrics():
    mst = timezone('MST')
    mst_now = datetime.now(mst)
    req = requests.get('https://squeezemetrics.com/monitor/static/DIX.csv?_t=1607864614116', timeout=300, stream=True)
    content = req.content.decode('utf-8')
    number = content.split()[-1].split(',')[1]
    data = {'date': content.split()[-1].split(',')[0], 'value green': content.split()[-1].split(',')[1],
            'value blue': float(content.split()[-1].split(',')[2])*100}
    latest = str(data['value blue'])
    current_dix = float(content.split()[-1].split(',')[2])*100
    the_dix_before_last = float(content.split()[-2].split(',')[2])*100
    gain_or_loss = str((((current_dix/the_dix_before_last)-1)*100).__round__(2))
    return latest, gain_or_loss


# vix_metrics()

