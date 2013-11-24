import eventbrite
from datetime import datetime
from collections import OrderedDict
import os
from settings import events_ids,USER_KEY,APP_KEY

eb_auth_tokens = {  'app_key': APP_KEY,
                    'user_key': USER_KEY}
eb_client = eventbrite.EventbriteClient(eb_auth_tokens)

events = {}
tsv = {}
tsv_file = 'date'

for k in events_ids:
    try:
        event = eb_client.event_get({'id':k})
    except:
        import sys
        sys.exit("A problem occurred during the connection, make sure your settings.py"+
                 " has the correct values (APP_KEY and USER_KEY).\n\n" +
                 "You can find this values on the Eventbrite website." )
    attendee_list = eb_client.event_list_attendees({'id':k, 'sort_by':'created'})

    tsv_file +=  '\t' + event['event']['start_date'][0:4]
    initial_date = datetime.strptime(event['event']['start_date'],'%Y-%m-%d %H:%M:%S')
    attendees_raw = attendee_list['attendees']

    data = {}

    for attendee in attendees_raw:

        date = datetime.strptime(attendee['attendee']['created'],'%Y-%m-%d %H:%M:%S')
        days_before = str(abs((initial_date - date).days))

        if days_before in data:
            data[days_before]['amount'] += float(attendee['attendee']['amount_paid'])
        else:
            data[days_before] = {}
            data[days_before]['amount'] = float(attendee['attendee']['amount_paid'])


    data = OrderedDict(sorted(data.items(), reverse=True, key=lambda t: int(t[0])))
    total = 0
    tsv[k] = {}

    for day in data:

        total += data[day]['amount']
        data[day]['total'] = total
        if not day in tsv:
            tsv[day] = {}
        tsv[day][k] = total

    events[k] = data

tsv = OrderedDict(sorted(tsv.items(), reverse=True, key=lambda t: int(t[0])))
previous = {}

for k in events_ids:
    tsv.popitem(last=False)

tsv_file += '\n'

for day in tsv:
    result = str(day) + '\t'
    for k in events_ids:
        if k in tsv[day]:
            result = result + str(tsv[day][k]) + '\t'
            previous[k] = str(tsv[day][k])
        else:
            if k in previous:
                result = result + previous[k] + '\t'
            else:
                result = result + '0' + '\t'
    tsv_file += result + '\n'



script_dir = os.path.dirname(os.path.abspath(__file__)) + '/data.tsv'
with open(script_dir, 'wb') as stream:
    stream.write(tsv_file)



