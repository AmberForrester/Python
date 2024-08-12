import json
from twilio.rest import Client

def load_contacts(filename='contacts.json'):
    with open(filename, 'r') as file:
        return json.load(file)
    
def check_events(contacts):
    from datetime import datetime
    today = datetime.today().strftime('%Y-%m-%d')
    today_events = [contact for contact in contacts if contact['event_date'] == today]
    return today_events

def send_sms(account_sid, auth_token, twilio_number, to_number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=twilio_number,
        to=to_number
    )
    print(f'Your special message has been sent {to_number}: {message.sid} Way to go, they are going to be so happy you remembered them!')