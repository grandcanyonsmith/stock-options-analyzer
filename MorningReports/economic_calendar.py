from twilio.rest import Client
from dix import *
account_sid = 'AC4edaa4f9768eb268b7907e9c2680d55d'
auth_token = '22cb9fa604d5051a11787b431f79201d'
client = Client(account_sid, auth_token)
client_phone_contact = ['+18016237631']
# client_phone_contact = ['+18016237631','+18018752975','+13852673595']
def send_client_text(sentence):
    for phone_number in client_phone_contact:
        message = client.messages.create(
                                body=sentence,
                                from_='+13852336341',
                                to=phone_number)
r = requests.get('https://finnhub.io/api/v1/calendar/economic?token=c1n20v237fkvp2lsh1ag')
for x in r.json()['economicCalendar']:
    latest, gain_or_loss = vix_metrics()
    if x['country'] == 'US':
        if x['impact'] != 'low':
            event = x['event']
            impact = x['impact']
            time = x['time']
            sentence = "On " + time + " " + event + " report will be released. Its results are estimated to have a "+ impact + " impact on the economy. Dix was "+ str(latest().__round__(2)) + "% yesterday. "+ str(gain_or_loss).__round__(2) + "%" + " higher than the previous day."
            message = x
            send_client_text(sentence)
            print(x)


# send_client_text()