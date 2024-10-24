from datetime import datetime, timedelta
from ics import Calendar, Event

# Create a new calendar
cal = Calendar()

# Define the base year for the schedule (2024/2025 academic year)
year = 2024

# Data for sign-up periods and payment dates
data = {
    "Month": ["April", "May", "June", "July", "August", "September", 
              "October", "November", "December", "January", "February", "March"],
    "Period to Sign-up": ["Mon.1 - Tue.9", "Wed.1 - Thu.9", "Mon.3 - Thu.6", 
                          "Mon.1 - Fri.5", "Thu.1 - Tue.6", "Mon.2 - Wed.4",
                          "Tue.1 - Tue.8", "Fri.1 - Thu.7", "Mon.2 - Wed.4",
                          "Mon.6 - Thu.9", "Mon.3 - Thu.6", "Mon.3 - Wed.5"],
    "The Date of Scholarship Payment": ["Thu.25", "Fri.24", "Mon.24", "Fri.25", 
                                        "Fri.23", "Thu.19", "Mon.28", "Mon.25", 
                                        "Thu.19", "Tue.28", "Wed.26", "Wed.19"]
}

# Define months and their numeric values
months = {
    "April": 4, "May": 5, "June": 6, "July": 7,
    "August": 8, "September": 9, "October": 10,
    "November": 11, "December": 12, "January": 1,
    "February": 2, "March": 3
}

# Function to parse period to sign up
def parse_signup_period(month, signup_period):
    start_day, end_day = signup_period.split(" - ")
    start_day = int(start_day.split('.')[1])
    end_day = int(end_day.split('.')[1])
    
    # Assuming that the period falls within the first 10 days of the month
    start_date = datetime(year, month, start_day)
    end_date = datetime(year, month, end_day)
    
    return start_date, end_date

# Function to create the ICS event
def create_event(name, start_date, end_date, all_day=True):
    event = Event(name=name, begin=start_date, end=end_date + timedelta(days=1))
    event.make_all_day()
    return event

# Add the sign-up periods and payment dates to the calendar
for i in range(len(data["Month"])):
    month = data["Month"][i]
    month_num = months[month]
    sign_up_start, sign_up_end = parse_signup_period(month_num, data["Period to Sign-up"][i])
    payment_day = int(data["The Date of Scholarship Payment"][i].split(".")[1])
    
    # Add sign-up event
    sign_up_event = create_event(f"{month} Scholarship Sign-Up Period", sign_up_start, sign_up_end)
    cal.events.add(sign_up_event)
    
    # Add payment date event
    payment_date = datetime(year, month_num, payment_day)
    payment_event = create_event(f"{month} Scholarship Payment", payment_date, payment_date)
    cal.events.add(payment_event)

# Save the calendar to an ICS file
ics_file_path = "scholarship_schedule.ics"
with open(ics_file_path, 'w') as f:
    f.writelines(cal)

print(f"ICS file generated: {ics_file_path}")