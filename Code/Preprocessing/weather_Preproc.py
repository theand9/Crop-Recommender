import pandas as pd
import numpy as np
import csv
import os
import string
import time


def dirNames(path):

    dirs_List = []
    file_List = []

    for roots, dirs, files in os.walk(path):  # SCAN FILES
        dirs_List.append(dirs)
        file_List.append(files)

    return dirs_List, file_List


def makePath(f_Path, dir_List, file_List):

    df_Fin = pd.DataFrame()

    for i in range(0, len(dir_List[0])):
        init_Path = os.path.join(f_Path, dir_List[0][i])
        for j in file_List[1]:
            fin_Path = os.path.join(init_Path, j)
            df_Csv = preProc(fin_Path, dir_List[0][i], j)

            df_Fin = df_Fin.append(df_Csv)

        df_Fin.to_csv(os.path.join(
            f_Path, f"{dir_List[0][i]}.csv"), index=False)
        df_Fin.drop(df_Fin.index, inplace=True)
        df_Fin = pd.DataFrame()


def preProc(fin_Path, param, dist_Name):
    df_Csv = pd.read_csv(fin_Path)
    df_Csv = df_Csv.rename(str.capitalize, axis='columns')

    filter1 = df_Csv["Year"] >= 1997.0
    df_Csv.where(filter1, inplace=True)
    df_Csv = df_Csv.dropna(how="all")

    dist_Name = os.path.splitext(dist_Name)[0]

    if param == "Rainfall":
        df_Csv["Whole Year"] = (df_Csv["Jan"] +
                                df_Csv["Feb"] + df_Csv["Mar"] +
                                df_Csv["Apr"] + df_Csv["May"] +
                                df_Csv["Jun"] + df_Csv["Jul"] +
                                df_Csv["Aug"] + df_Csv["Sep"] +
                                df_Csv["Oct"] + df_Csv["Nov"] + df_Csv["Dec"])

        df_Csv["Kharif"] = (df_Csv["Jun"] +
                            df_Csv["Jul"] + df_Csv["Aug"] +
                            df_Csv["Sep"] + df_Csv["Oct"])

        df_Csv["Rabi"] = (df_Csv["Oct"] +
                          df_Csv["Nov"] + df_Csv["Dec"] +
                          df_Csv["Jan"] + df_Csv["Feb"])

    else:
        df_Csv["Whole Year"] = (df_Csv["Jan"] +
                                df_Csv["Feb"] + df_Csv["Mar"] +
                                df_Csv["Apr"] + df_Csv["May"] +
                                df_Csv["Jun"] + df_Csv["Jul"] +
                                df_Csv["Aug"] + df_Csv["Sep"] +
                                df_Csv["Oct"] + df_Csv["Nov"] +
                                df_Csv["Dec"]) / 12

        df_Csv["Kharif"] = (df_Csv["Jun"] +
                            df_Csv["Jul"] + df_Csv["Aug"] +
                            df_Csv["Sep"] + df_Csv["Oct"]) / 5

        df_Csv["Rabi"] = (df_Csv["Oct"] +
                          df_Csv["Nov"] + df_Csv["Dec"] +
                          df_Csv["Jan"] + df_Csv["Feb"]) / 5

    cols_Drop = ["Jan", "Feb", "Mar", "Apr", "May",
                 "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_Csv = df_Csv.drop(cols_Drop, axis=1)

    if param == "Temperature":
        df_Csv = df_Csv.drop("Unnamed: 0", axis=1)

    elif param == "Humidity":
        df_Csv = df_Csv.drop(["Unnamed: 0", "Unnamed: 0.1"], axis=1)

    df_Csv = pd.melt(df_Csv, id_vars=["Year"],
                     var_name=["Season"], value_name="Record")
    df_Csv["District"] = dist_Name

    return df_Csv


if __name__ == "__main__":
    # Path to import file
    main_Path = "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Weather/"
    dir_List, file_List = dirNames(main_Path)

    makePath(main_Path, dir_List, file_List)
