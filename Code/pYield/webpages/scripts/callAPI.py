import requests
import json
import re
import pandas as pd
from datetime import datetime
from dateutil import parser
import random
from heapq import nlargest
from webpages.models import *


def weatherAPI(farmer_District):
    api_Key = 'fa1b47d86b1b6f9b0a5568a5b8900a1e'
    temp, humid = 0, 0

    for i in districtCoords.objects.raw(
            "SELECT District, Latitude, Longitude from webpages_districtCoords WHERE District = %s", [farmer_District.capitalize()]):
        pass

    for j in rainfall2k19.objects.raw("SELECT district, rainfall from webpages_rainfall2k19 WHERE district= %s", [farmer_District.capitalize()]):
        pass

    Longitude, Latitude = i.Longitude, i.Latitude
    rain = j.rainfall

    url = f"https://api.darksky.net/forecast/{api_Key}/{Latitude},{Longitude}?units=ca&exclude=currently,minutely,hourly,flags"

    json_Data = requests.get(url).json()
    daily_Data = json_Data["daily"]["data"]

    for i in daily_Data:
        weather_Data = [i[j] for j in i if j in [
            "temperatureHigh", "temperatureLow", "humidity"]]

        temp += weather_Data[0] + weather_Data[1]
        humid += weather_Data[2]

    temp = round(temp / 14, 3)
    humid = round((humid / 7) * 100, 3)

    return temp, humid, rain


def soilVals(farmer_Dist, farmer_Village):  # Soil Data------------------
    soil_Data = []

    if farmer_Dist.capitalize() == "Akola":
        for i in Akola.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Akola WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Amravati":
        for i in Amravati.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Amravati WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Aurangabad":
        for i in Aurangabad.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Aurangabad WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Beed":
        for i in Beed.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Beed WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Bhandara":
        for i in Bhandara.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Bhandara WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Buldhana":
        for i in Buldhana.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Buldhana WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Chandrapur":
        for i in Chandrapur.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Chandrapur WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Dhule":
        for i in Dhule.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Dhule WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Gadchiroli":
        for i in Gadchiroli.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Gadchiroli WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Gondia":
        for i in Gondia.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Gondia WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Hingoli":
        for i in Hingoli.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Hingoli WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Jalgaon":
        for i in Jalgaon.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Jalgaon WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Jalna":
        for i in Jalna.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Jalna WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Kolhapur":
        for i in Kolhapur.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Kolhapur WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Latur":
        for i in Latur.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Latur WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Nagpur":
        for i in Nagpur.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Nagpur WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Nanded":
        for i in Nanded.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Nanded WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Nandurbar":
        for i in Nandurbar.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Nandurbar WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Nashik":
        for i in Nashik.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Nashik WHERE village_Name = %s", [farmer_Village.upper()]):
            print("hey2")
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Osmanabad":
        for i in Osmanabad.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Osmanabad WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Parbhani":
        for i in Parbhani.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Parbhani WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Pune":
        for i in Pune.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Pune WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Raigad":
        for i in Raigad.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Raigad WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Ratnagiri":
        for i in Ratnagiri.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Ratnagiri WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Sangli":
        for i in Sangli.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Sangli WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Satara":
        for i in Satara.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Satara WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Sindhudurg":
        for i in Sindhudurg.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Sindhudurg WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Solapur":
        for i in Solapur.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Solapur WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Thane":
        for i in Thane.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Thane WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Wardha":
        for i in Wardha.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Wardha WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Washim":
        for i in Washim.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Washim WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    if farmer_Dist.capitalize() == "Yavatmal":
        for i in Yavatmal.objects.raw("SELECT village_Name, ph_Value, N_Value, P_Value, K_Value, OC_Value, Fe_Value from webpages_Yavatmal WHERE village_Name = %s", [farmer_Village.upper()]):
            soil_Data.extend([i.ph_Value, i.N_Value, i.P_Value,
                              i.K_Value, i.OC_Value, i.Fe_Value])

    return soil_Data


def farmerDetails(aadhar_Number):
    farmer_Info = farmerRegistration.objects.get(
        aadhar_Number=aadhar_Number)

    farmer_List = [farmer_Info.farmer_Name, farmer_Info.phone_Number,
                   farmer_Info.areaInHectare, farmer_Info.aadhar_Number, farmer_Info.district, farmer_Info.village]

    return farmer_List


def getSeason():
    now_DT = datetime.now()
    month = now_DT.strftime("%m")
    today = now_DT.strftime("%d-%m-%Y %I:%M:%S")

    if int(month) in [4, 5, 6, 7, 8]:
        return "Kharif", today

    if int(month) in [1, 2, 10, 11, 12]:
        return "Rabi", today

    else:
        return None, today


def cropData(season):

    crop_List, grow_Time, crop_Name = [], [], []

    for i in Crop_List.objects.raw("SELECT * from webpages_Crop_List WHERE season = %s OR season = 'Whole Year'", [season.capitalize()]):
        crop_List.append([i.crop_Arhar, i.crop_Bajra, i.crop_Cotton, i.crop_Gram, i.crop_Groundnut, i.crop_Jowar, i.crop_Maize, i.crop_Moong, i.crop_Mustard,
                          i.crop_Nigerseed, i.crop_Ragi, i.crop_Rice, i.crop_Safflower, i.crop_Sesamum, i.crop_Soyabean, i.crop_Sugarcane, i.crop_Sunflower, i.crop_Urad, i.crop_Wheat])
        crop_Name.append(i.crop)

    for j in seasonEncode.objects.raw("SELECT * from webpages_seasonEncode WHERE seasonName = %s", [season.capitalize()]):
        pass

    season_Data = [j.kharif, j.rabi, j.wholeYear]

    return crop_List, season_Data, crop_Name


def flaskAPI(soil_Data, rain, temp, humid, season, crop_Data, crop):
    url = 'http://localhost:9999/api/'
    predict_Profit = {}
    crop_Name, crop_Profit, crop_Gtime = [], [], []

    for i in range(0, len(crop_Data)):
        if crop_Data[i] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]:
            final_Data = [[rain, temp, humid, random.randrange(
                0, 2)] + soil_Data + season + crop_Data[i]]

        else:
            final_Data = [[rain, temp, humid, random.randrange(
                0, 2)] + soil_Data + [0, 0, 1] + crop_Data[i]]

        j_data = json.dumps(final_Data)

        headers = {'content-type': 'application/json',
                   'Accept-Charset': 'UTF-8'}

        predict_Data = requests.post(url, data=j_data, headers=headers)
        result = float(re.sub('[^0-9|.]', '', predict_Data.text))

        predict_Profit[crop[i]] = result

    highest_Vals = nlargest(3, predict_Profit, key=predict_Profit.get)
    for val in highest_Vals:
        crop_Name.append(val)
        crop_Profit.append(predict_Profit.get(val))

        for i in Crop_List.objects.raw("SELECT * from webpages_Crop_List WHERE crop = %s", [crop_Name[-1]]):
            crop_Gtime.append(i.time_to_Grow)

    return crop_Name, crop_Profit, crop_Gtime


def run(aadhar_Number):
    farmer_List = farmerDetails(aadhar_Number)

    curr_Temp, curr_Humid, curr_Rain = weatherAPI(farmer_List[4])
    soil_Data = soilVals(farmer_List[4], farmer_List[5])

    season, curr_Date = getSeason()
    crop_List, season_Data, crop_Name = cropData(season)

    crop_List = [[int(x) for x in i]
                 for i in crop_List]  # Nested Lists
    season_Data = [int(i) for i in season_Data]

    crop_List, crop_Profit, crop_Gtime = flaskAPI(
        soil_Data, curr_Rain, curr_Temp, curr_Humid, season_Data, crop_List, crop_Name)

    curr_Date = parser.parse(curr_Date)

    if season.lower() == "kharif":
        date_Diff = datetime(2019, 6, 20) - curr_Date

    elif season.lower() == "rabi":
        date_Diff = datetime(2019, 12, 10) - curr_Date

    else:
        date_Diff = 0

    return farmer_List, curr_Date, crop_List, crop_Profit, season, crop_Gtime, date_Diff.days
