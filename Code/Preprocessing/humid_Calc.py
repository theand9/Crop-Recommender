import pandas as pd
import numpy as np
import csv
import os
import string


def dirNames(path):

    dirs_List = []
    file_List = []

    for roots, dirs, files in os.walk(path):  # SCAN FILES
        dirs_List.append(dirs)
        file_List.append(files)

    return dirs_List, file_List


def makePath(path, dir_List, file_List):

    for i in range(0, len(file_List[1])):
        init_Path1 = os.path.join(path, dir_List[0][0])
        final_Path1 = os.path.join(init_Path1, file_List[1][i])

        init_Path2 = os.path.join(path, dir_List[0][-1])
        final_Path2 = os.path.join(init_Path2, file_List[1][i])

        df_Humid = procHumid(final_Path1, final_Path2)

        init_Path3 = os.path.join(path, dir_List[0][1])
        final_Path3 = os.path.join(init_Path3, file_List[1][i])
        saveFile(final_Path3, df_Humid)


def saveFile(save_Path, df_Fin):

    df_Fin.to_csv(save_Path)
    df_Fin.drop(df_Fin.index, inplace=True)
    df_Fin = pd.DataFrame()
    print("Done")


def procHumid(path1, path2):

    df_Temp = pd.read_csv(path2)
    df_VapPress = pd.read_csv(path1)
    df_Humid = pd.DataFrame()

    df_Vap_Dict = df_VapPress.to_dict("list")
    df_Temp_Dict = df_Temp.to_dict("list")
    df_Humid_Dict = {}

    for i in df_Vap_Dict:
        df_Humid_Dict[i] = []

    df_Humid_Dict["Year"] = df_Vap_Dict["Year"]
    for i in df_Vap_Dict:
        if i != "Year":
            for j in range(0, len(df_Vap_Dict[i])):
                df_Humid_Dict[i].append(
                    (df_Vap_Dict[i][j] / (101 ** ((7.5 * df_Temp_Dict[i][j]) / (237.7 + df_Temp_Dict[i][j])))) * 100)

    df_Humid = df_Humid.from_dict(df_Humid_Dict)

    return df_Humid


if __name__ == "__main__":
    # Path to import file
    main_Path = "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Weather/"
    dir_List, file_List = dirNames(main_Path)

    makePath(main_Path, dir_List, file_List)
