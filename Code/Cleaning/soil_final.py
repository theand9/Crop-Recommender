import numpy as np
import pandas as pd
import os


def fileNames(path):

    file_List = []

    for roots, dirs, files in os.walk(path):  # SCAN FILES
        file_List.append(files)

    return file_List


def makePath(path, file_List):
    for i in file_List[0]:
        f_Path = os.path.join(path, i)
        df_Csv = finalClean(f_Path)

        clean_File_Path = f"C:/Users/amogh/Desktop/Soil/{i}"
        df_Csv.to_csv(clean_File_Path, index=False)


def finalClean(f_Path):
    df_Csv = pd.read_csv(f_Path)
    df_Csv.drop_duplicates("Village", keep="first", inplace=True)

    return df_Csv


if __name__ == "__main__":

    f_Path = "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Soil"
    file_List = fileNames(f_Path)

    makePath(f_Path, file_List)
