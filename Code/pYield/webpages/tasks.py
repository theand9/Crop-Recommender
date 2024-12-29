import time
import re
from datetime import datetime
import requests
import pandas as pd
import os

from . import models
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(day_of_week='sunday')),
    name="initAll",
    ignore_result=True
)
def createURL():

    api_Key = 'fa1b47d86b1b6f9b0a5568a5b8900a1e'

    dist_List = ['Akola', 'Amravati', 'Aurangabad', 'Beed', 'Bhandara',                     'Buldhana', 'Chandrapur', 'Dhule', 'Gadchiroli', 'Gondia',                 'Hingoli', 'Jalgaon', 'Jalna', 'Kolhapur', 'Latur', 'Nagpur',
                 'Nanded', 'Nandurbar', 'Nashik', 'Osmanabad', 'Parbhani',     'Pune', 'Raigad', 'Ratnagiri', 'Sangli', 'Satara',            'Sindhudurg', 'Solapur', 'Thane', 'Wardha', 'Washim',         'Yavatmal']

    for district in dist_List:
        dist_Data = models.districtCoords.objects.get(District=district)

        url = f"https://api.darksky.net/forecast/{api_Key}/{dist_Data.Latitude},{dist_Data.Longitude}?units=ca&exclude=currently,minutely,hourly,flags"

        getData(url, dist_Data.District)


def getData(req_URL, dist_Name):

    json_Data = requests.get(req_URL).json()
    daily_Data = json_Data["daily"]["data"]
    f_Path = "C:/Users/amogh/Desktop/file1.txt"

    with open(f_Path, "w+") as file1:
        file1.write(f"\n{dist_Name}: {json_Data['daily']['summary']} \n")
        for i in daily_Data:
            weather_Data = [i[j] for j in i if (j in [
                "time", "summary", "precipIntensity", "precipProbability", "temperatureHigh", "temperatureLow", "humidity", "windGust", "cloudCover"])]

            msg_Data = f"""\t{datetime.utcfromtimestamp(int(weather_Data[0])).strftime('%d-%m-%Y')} -> {weather_Data[1]}
            Rainfall:
                Probability: {weather_Data[3]}
                Intensity: {weather_Data[2]} mm
            Temperature:
                Max: {weather_Data[4]} C
                Min: {weather_Data[5]} C
            Humidity: {weather_Data[6] * 100}%
            Max Wind Speed: {weather_Data[7]} km/h
            Cloud Cover: {weather_Data[8] * 100} % \n"""

            file1.write(msg_Data)

    sendMsg(dist_Name)


def sendMsg(dist_Name):

    # Insert database query and send message code here
    f_Path = "C:/Users/amogh/Desktop/file1.txt"
    with open(f_Path, "r+") as file1:
        msg_Data = file1.read()
        msg_Data = re.sub(r'[^\x00-\x7f]', r' ', msg_Data)

    farmer_List = models.farmerRegistration.objects.filter(
        district=dist_Name)

    for farmer in farmer_List:
        msg_API_URL = "https://www.fast2sms.com/dev/bulk"
        payload = f"sender_id=FSTSMS&message={msg_Data}&language=english&route=p&numbers={farmer.phone_Number}"
        headers = {
            "authorization": '8TkVdJzsDjiM0bkk333tJUGFsTfc84JxMfFMGgeRGRwC63FhtbyIbsHERBDv',
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache"
        }

        response = requests.request(
            "POST", msg_API_URL, data=payload, headers=headers)
        print(response.text)

    os.remove(f_Path)

# For testing of scheduler only
# @periodic_task(
#     run_every=crontab(),
#     name="createFile",
#     ignore_result=True
# )
# def createFile():
#     with open("C://Users/amogh/Desktop/newtxt.txt", "w+") as file1:
#         file1.writelines("Hii")
#         file1.writelines("Scheduling WORKSSSS!!!!!!!!")
