import numpy as np
import pandas as pd
import os
import random


def fileNames(path):

    dirs_List = []
    file_List = []

    for roots, dirs, files in os.walk(path):  # SCAN FILES
        dirs_List.append(dirs)
        file_List.append(files)

    return dirs_List, file_List


def makePath(f_Path, dirs_List, file_List):

    for i in range(0, len(dirs_List[0])):
        init_Path = os.path.join(f_Path, dirs_List[0][i])
        for j in file_List[1]:
            fin_Path = os.path.join(init_Path, j)
            fileClean(fin_Path)


def fileClean(path):
    df_Csv = pd.read_csv(path)

    list1 = list(df_Csv.std())
    list1.remove(max(list1))

    for i in range(2003, 2015):
        random.seed(random.randrange(1, 10000))
        df_Temp = df_Csv.mean() + random.uniform(-max(list1), max(list1))
        df_Temp["Year"] = i

        df_Csv = df_Csv.append(df_Temp, ignore_index=True)

    df_Csv.to_csv(path)


if __name__ == "__main__":
    f_Path = "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Weather/"

    dirs_List, file_List = fileNames(f_Path)
    makePath(f_Path, dirs_List, file_List)
