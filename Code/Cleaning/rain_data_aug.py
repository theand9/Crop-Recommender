import os
import pandas as pd
import numpy as np


def cleanOgFile(f_Path, rain_Path):

    df_Temp = pd.read_csv(f_Path)

    list1 = ['ANDAMAN & NICOBAR ISLANDS', 'ARUNACHAL PRADESH',
             'ASSAM & MEGHALAYA', 'NAGALAND, MANIPUR, MIZORAM,TRIPURA',
             'SUB-HIMALAYAN W BENGAL & SIKKIM', 'GANGETIC WEST BENGAL',
             'ORISSA', 'JHARKHAND', 'BIHAR ', 'EAST UTTAR PRADESH',
             'WEST UTTAR PRADESH', 'UTTARANCHAL', 'HARYANA, DELHI & CHANDIGARH',
             'PUNJAB ', 'HIMACHAL PRADESH', 'JAMMU & KASHMIR',
             'WEST RAJASTHAN ', 'EAST  RAJASTHAN ', 'WEST MADHYA PRADESH',
             'EAST MADHYA PRADESH', 'GUJARAT REGION, DADRA & NAGAR HAVELI',
             'SAURASHTRA KUTCH & DIU', 'CHATTISGARH', 'COSTAL ANDHRA PRADESH',
             'TELENGANA', 'RAYALSEEMA', 'TAMIL NADU & PONDICHERRY',
             'COASTAL KARNATAKA', 'NORTH INTERIOR KARNATAKA',
             'SOUTH INTERIOR KARNATAKA', 'KERALA', 'LAKSHADWEEP ']

    for i in list1:
        df_Temp.where(df_Temp["SD_Name"] != i, inplace=True)

    df_Temp.where(df_Temp["YEAR"] > 2002.0, inplace=True)
    df_Temp = df_Temp.dropna()

    cols_Drop = ["SD NO.", "ANNUAL", "JAN-FEB",
                 "Mar-May", "Jun-Sep", "Oct-Dec"]
    df_Temp = df_Temp.drop(cols_Drop, axis=1)
    df_Temp = df_Temp.rename(str.capitalize, axis='columns')

    df_Temp["Sd_name"].replace(['KOKAN & GOA', 'MADHYA MAHARASHTRA',                                      'MARATWADA ', 'VIDARBHA'], [
                               'Konkan', 'Madhya Maharashtra', 'Maratwada', 'Vidharbha'], inplace=True)

    vidarbha = ['Amravati.csv', 'Akola.csv', 'Bhandara.csv', 'Buldana.csv',               'Chandrapur.csv',
                'Gadchiroli.csv', 'Gondiya.csv', 'Nagpur.csv', 'Wardha.csv', 'Washim.csv', 'Yatavmal.csv']
    maratwada = ['Jalna.csv', 'Aurangabad.csv', 'Parbhani.csv',
                 'Hingoli.csv', 'Nanded.csv', 'Latur.csv', 'Osmanabad.csv', 'Bid.csv']
    madhya_Maha = ['Dhule.csv', 'Jalgaon.csv', 'Kohlapur.csv', 'Nandurbar.csv',
                   'Nashik.csv', 'Pune.csv', 'Sangli.csv', 'Satara.csv', 'Solapur.csv']
    konkan = ["Raigad.csv", "Ratnagiri.csv", "Thane.csv", "Sindhudurg.csv"]

    region_Names = df_Temp.Sd_name.unique()
    print(region_Names)
    for i in region_Names:
        sub_Df = df_Temp[df_Temp.Sd_name == i]

        if sub_Df.Sd_name.unique() == "Vidharbha":
            sub_Df = sub_Df.drop("Sd_name", axis=1)
            for j in vidarbha:
                new_Path = os.path.join(rain_Path, j)
                df_Rain = pd.read_csv(new_Path)
                df_Fin = pd.concat([df_Rain, sub_Df], join="inner")

                df_Fin = df_Fin[["Year", "Jan", "Feb", "Mar", "Apr",
                                 "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]]

                df_Fin.to_csv(new_Path, index=False)

        elif sub_Df.Sd_name.unique() == "Maratwada":
            sub_Df = sub_Df.drop("Sd_name", axis=1)
            for j in maratwada:
                new_Path = os.path.join(rain_Path, j)
                df_Rain = pd.read_csv(new_Path)
                df_Fin = pd.concat([df_Rain, sub_Df], join="inner")

                df_Fin = df_Fin[["Year", "Jan", "Feb", "Mar", "Apr",
                                 "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]]

                df_Fin.to_csv(new_Path, index=False)

        elif sub_Df.Sd_name.unique() == "Madhya Maharashtra":
            sub_Df = sub_Df.drop("Sd_name", axis=1)
            for j in madhya_Maha:
                new_Path = os.path.join(rain_Path, j)
                df_Rain = pd.read_csv(new_Path)
                df_Fin = pd.concat([df_Rain, sub_Df], join="inner")

                df_Fin = df_Fin[["Year", "Jan", "Feb", "Mar", "Apr",
                                 "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]]

                df_Fin.to_csv(new_Path, index=False)

        elif sub_Df.Sd_name.unique() == "Konkan":
            sub_Df = sub_Df.drop("Sd_name", axis=1)
            for j in konkan:
                new_Path = os.path.join(rain_Path, j)

                df_Fin = sub_Df[["Year", "Jan", "Feb", "Mar", "Apr",
                                 "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]]

                df_Fin.to_csv(new_Path, index=False)


if __name__ == "__main__":
    f_Path = "C:/Users/amogh/Downloads/datafile (1).csv"
    rain_Path = "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Weather/Rainfall/"

    cleanOgFile(f_Path, rain_Path)
