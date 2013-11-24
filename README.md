eventbrite_compare
==================

A simple script that connects to eventbrite and compares different events income,
based on how many days are left for the event.

The script generates a data.tsv file that can be loaded with the html file also included,
and will show a line chart containing the progression of the event.

If the event has not being held yet, a grey area will cover how many days are left.

## Libraries I used

###Script
[Eventbrite](https://github.com/eventbrite/eventbrite-client-py)

###HTML
[d3.js](http://d3js.org/)

[Jquery](http://jquery.com/)



## Instructions:

#### 1. SETUP

Connect to your eventbrite account and fill the settings.py document with your data:

[APP_KEY](https://www.eventbrite.com/api/key) = 'XXXXXXXXXXXXXXXXXX'


[USER_KEY](https://www.eventbrite.com/userkeyapi) = '000000000000000000000'

Once you connect to the website, select your event and you'll find the id on the url (eid)
You also can use the API to list all the events available
https://www.eventbrite.com/myevent?eid=XXXXXXXXXX

events_ids = [000000001, 000000002]

#### 2. EXECUTE

```python compare.py```

This command will generate a data.tsv file with all the retrieved data from eventbrite.

#### 3. SHOW RESULTS

Open the index.html on your web browser to compare the results.

###I hope it helps someone!

Find below some images:

![alt tag](https://raw.github.com/xavicolomer/eventbrite_compare/master/README/comparison2.jpg)
![alt tag](https://raw.github.com/xavicolomer/eventbrite_compare/master/README/comparison.png)
