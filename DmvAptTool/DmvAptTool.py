from bs4 import BeautifulSoup
import requests
import time
import os

def get_time_slot(path, locations):
    for id in locations:
        url = path + str(id)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        try:
            appt_list = soup.find(id='timeslots')
            if appt_list.a.div['class'][1] == "availableTimeslot":
                print(soup.main.find('ul').li.get_text())
                print(url)
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                print(current_time)
                os.system('say "Found an appointment"')
                os.system('say "Found an appointment"')
                os.system('say "Found an appointment"')
        except Exception:
            continue

path = "https://telegov.njportal.com/njmvc/AppointmentWizard/15/"
locations = range(186, 208)
while True:

    get_time_slot(path, locations)
    time.sleep(60)


