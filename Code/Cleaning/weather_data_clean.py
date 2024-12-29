import pandas as pd
import numpy as np
import os
import csv


def dirNames(path):

    dirs_List = []

    for roots, dirs, files in os.walk(path):  # SCAN FILES
        dirs_List.append(dirs)

    return dirs_List


def makePath(path, dir_List):

    i = 0
    while i < len(dir_List[0]):
        j = 0
        while j < len(dir_List[1]):
            init_Path = os.path.join(path, dir_List[0][i])
            mid_Path = os.path.join(init_Path, dir_List[1][j])
            final_Path = os.path.join(mid_Path, "data.csv")

            clean_File_Path = f"C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Weather/{dir_List[0][i]}/{dir_List[1][j]}.csv"

            cleanFiles(clean_File_Path, final_Path)

            j += 1
        i += 1


def cleanFiles(clean_File_Path, final_Path):

    inputFile = csv.reader(open(final_Path, "r+"), delimiter="\t")
    csv.register_dialect("clean", quoting=csv.QUOTE_NONE,
                         delimiter=',', escapechar="\t")

    with open(clean_File_Path, "w+") as clean_File:
        add_Cleaned_Rows = csv.writer(clean_File, dialect="clean")
        for row in inputFile:
            add_Cleaned_Rows.writerow(row)

    clean_File.close()


if __name__ == "__main__":
    path = "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Weather/"

    dir_List = dirNames(path)

    makePath(path, dir_List)
