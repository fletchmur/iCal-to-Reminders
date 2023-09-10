import icalendar
import datetime

calendar_file_name = "Discrete Structure.ics"

def parse_ical(file_name):

    events = []
    with open(file_name) as f:
        calendar = icalendar.Calendar.from_ical(f.read())

        for event in calendar.walk('VEVENT'):
            summary = event.get('Summary').replace('\n', ' ')
            ical_date_time = event['DTSTART'].to_ical()
            #lots of formatting to get into the correct format to create into a vDate
            ical_date = str(ical_date_time).split("T")[0].replace("b","").replace("'","")
            dt = icalendar.vDate.from_ical(ical_date)
            
            start_date = str(dt.month) + '/' + str(dt.day) + '/' + str(dt.year)

            events.append(f"{summary} \n{start_date}\n")

    return events

def write_assignment_text(file_name, class_tag, event_list):
    with open(file_name, 'a') as f:
        f.write(class_tag + "\n")
        for event in event_list:
            f.write(event)

assignments = parse_ical(calendar_file_name)
print(assignments)
write_assignment_text("test.txt","Book of Mormon",assignments)




