import os
from dotenv import load_dotenv
from datetime import datetime
from utils import load_contacts, check_events, send_sms 

# Loading environment variables (Twilio Credentials) from .env file -
load_dotenv()

# Twilio credentials from .env file:
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
my_phone_number = os.getenv('MY_PHONE_NUMBER')

# Load contacts - 
contacts = load_contacts()

# Check for any special events happening today - 
today_events = check_events(contacts)

if today_events:
    for event in today_events:
        event_type = event['event_type']
        message = f'Hey Amber!!! Don\'t forget to message or call {event['name']} NOW before you get busy with your day and forget! It is their {event_type} today and {event['memory']} I know {event['name']} will enjoy getting a special message from you!'
        send_sms(account_sid, auth_token, twilio_number, my_phone_number, message)
else: 
    print('None of your friends and family have any special events today, but if something new pops up don\'t forget to update your Contact list so you never forget!')