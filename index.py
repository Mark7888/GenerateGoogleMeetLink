from googleapiclient.discovery import build
import pickle
from datetime import datetime

credentials = pickle.load(open("token.pkl", "rb"))

service = build("calendar", "v3", credentials=credentials)

result = service.calendarList().list().execute()

calendar_id = result['items'][0]['id']

start_time = datetime(2020, 6, 23, 20, 15, 0)
end_time = datetime(2020, 6, 23, 20, 30, 0)

event = {
  'summary': 'Session Meet Link',
  'location': 'Mumbai',
  'description': 'Class',
  'start': {
    'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'Asia/Kolkata',
  },
  'end': {
    'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'Asia/Kolkata',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=1'
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
  'conferenceData': {
      'createRequest' : {
          'requestId' : "divya"
      }
  },
}

result = service.events().insert(calendarId=calendar_id, conferenceDataVersion=1, body=event).execute()

link = result['hangoutLink']

print(link)
