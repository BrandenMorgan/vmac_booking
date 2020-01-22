import sys
from apiclient.discovery import build  # Oauth 2.0 setup
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta
import datefinder

scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file('../client_secret.json', scopes=scopes)
credentials = flow.run_console()
pickle.dump(credentials, open("token.pkl", "wb"))
credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)

# Get my calendars
result = service.calendarList().list().execute()
# print(result['items'][4])

# Get my calendar events
calendar_id = result['items'][4]['id']
result = service.events().list(calendarId=calendar_id).execute()
# Get event id
event_id = result['items'][2]['id']

start_time = datetime(2020, 1, 15, 19, 30, 0)
end_time = start_time + timedelta(hours=4)
timezone = 'America/Los_Angeles'


# Create new calendar event
event = {
  'summary': 'Vmac reservation practice',
  'location': '800 Howard St., Portland, OR 97212',
  'description': 'Scheduling events.',
  'start': {
    'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'end': {
    'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

service.events().insert(calendarId=calendar_id, body=event).execute()

matches = datefinder.find_dates('15 january 7:30 PM')


def create_event(start_time_str, summary, duration=1, description=None, location=None):
  matches = list(datefinder.find_dates(start_time_str))
  if len(matches):
    start_time = matches[0]
    end_time = start_time + timedelta(hours=duration)
  event = {
    'summary': summary,
    'location': location,
    'description': description,
    'start': {
      'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
      'timeZone': timezone,
    },
    'end': {
      'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
      'timeZone': timezone,
    },
    'reminders': {
      'useDefault': False,
      'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
      ],
    },
  }
  print('before event')
  print(event)
  return service.events().insert(calendarId='primary', body=event).execute()


create_event('21 january 18:00', 'coffee time')
