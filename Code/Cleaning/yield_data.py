import pandas as pd
import numpy as np
import os
import csv


def iqrClean(data_List):
    """
    Summary:
            To clean outliers from data using IQR, more accurate

    Arguments:
            data_List {list} -- Sub-setted village-wise list

    Returns:
            data_List {list} -- Cleaned list subset
    """

    sorted(data_List)  # Sort data to find IQR

    lower_Quartile, upper_Quartile = np.percentile(
        data_List, [10, 90])  # Finding upper and lower quartile
    iqr = upper_Quartile - lower_Quartile  # Finding inter-quartile range
    lower_Bound = lower_Quartile - (iqr * 2.25)  # Find lower bound/level
    upper_Bound = upper_Quartile + (iqr * 2.25)  # Find upper bound/level

    for data in range(0, len(data_List)):   # To iterate over whole data_List
        # Check if data is out of bounds
        if (data_List[data] > upper_Bound) | (data_List[data] < lower_Bound):
            data_List[data] = np.nan  # Make out of bounds data Nan

    return data_List  # Return Data List


def dataClean(path):

    df_Temp = pd.DataFrame()
    df_Csv = pd.read_csv(path)
    farm_Yield = df_Csv.Production / df_Csv.Area
    df_Csv["Yield"] = farm_Yield.where(
        df_Csv.State_Name == 'Maharashtra')

    df_Csv = df_Csv.astype({"Crop_Year": "int64"})
    df_Csv = df_Csv.drop("Sr No.", axis=1)

    filter1 = df_Csv["Yield"] >= 0.1
    filter2 = df_Csv["Area"] > 25.0
    df_Csv.where(filter1 & filter2, inplace=True)
    df_Csv = df_Csv.dropna(how="all")

    dist_List = df_Csv.District_Name.unique()
    crop_List = df_Csv.Crop.unique()

    for i in dist_List:
        for j in crop_List:
            df_Sub = df_Csv[(df_Csv.District_Name == i) & (df_Csv.Crop == j)]
            df_Sub_Dict = df_Sub.to_dict("list")

            if len(df_Sub_Dict["Yield"]) > 5:
                df_Sub_Dict["Yield"] = iqrClean(df_Sub_Dict["Yield"])
                df_Temp = df_Temp.append(df_Temp.from_dict(
                    df_Sub_Dict))

    df_Temp = df_Temp.dropna(how="any")
    df_Temp = df_Temp.reset_index(drop=True)
    df_Temp.to_csv(
        "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Crops/finaldata.csv", index_label="Index")


if __name__ == "__main__":

    path = "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Crops/finalcrop.csv"

    dataClean(path)
