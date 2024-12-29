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


def makePath(path, dir_List, file_List):

    df_Fin = pd.DataFrame()
    i = 0

    for j in range(1, len(file_List)):
        while i < len(dir_List[0]):
            init_Path = os.path.join(path, dir_List[0][i])
            for k in file_List[j]:
                fin_Path = os.path.join(init_Path, k)
                print(fin_Path)
                df_Csv = dataClean(fin_Path)
                df_Fin = df_Fin.append(df_Csv)

            clean_File_Path = f"../Dataset/Final soil_Village/{dir_List[0][i]}.csv"
            saveFile(clean_File_Path, df_Fin)
            i += 1
            break


# def z_score_Clean(data_List):


# """
#     Summary:
#             To clean outliers from data using z-score, less accurate

#     Arguments:
#             data_List {list} -- Sub-setted village-wise list

#     Returns:
#             data_List {list} -- Cleaned list subset
#     """
# threshold = 3.5
#  median_y = np.median(data_List)
#   median_absolute_deviation_y = np.median(
#        [np.abs(data - median_y) for data in data_List])

#    for data in data_List:
#         modified_z_scores = [
#             0.55 * (data - median_y) / median_absolute_deviation_y]
#         if np.abs(modified_z_scores) > threshold:
#             data_List[data] = np.nan

#     return data_List


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
        data_List, [25, 75])  # Finding upper and lower quartile
    iqr = upper_Quartile - lower_Quartile  # Finding inter-quartile range
    lower_Bound = lower_Quartile - (iqr * 1.95)  # Find lower bound/level
    upper_Bound = upper_Quartile + (iqr * 1.95)  # Find upper bound/level

    for data in range(0, len(data_List)):   # To iterate over whole data_List
        # Check if data is out of bounds
        if (data_List[data] > upper_Bound) | (data_List[data] < lower_Bound):
            data_List[data] = np.nan  # Make out of bounds data Nan

    return data_List  # Return Data List


def dataClean(csv_Path):
    # Load file into DataFrame df_Csv
    df_Csv = pd.read_csv(csv_Path, skiprows=3)

    df_Csv = df_Csv.dropna(axis=1, how="all")  # Drop all blank columns
    # filter_Cond cond1 drop columns whose first index of sample no is not M
    filter_Cond1 = df_Csv["Sample No."].str[0] == "M"
    # filter_Cond cond2 drop columns whose first index of sample no is not V
    filter_Cond2 = df_Csv["Sample No."].str[0] == "V"
    df_Csv.where(filter_Cond1 | filter_Cond2, inplace=True)
    df_Csv = df_Csv.dropna(how="all")  # Drop all rows with NaN"s

    df_Csv = df_Csv.reset_index(drop=True)  # Reset index for consistency
    df_Temp1 = df_Csv.copy()  # Create a deep copy of df_Csv to df_Temp1

    # filter_Cond cond1 drop columns whose first index of sample no is not M again used to filter_Cond out village name
    filter_Cond1 = df_Csv["Sample No."].str[0] == "M"
    df_Csv.where(filter_Cond1, inplace=True)
    df_Csv = df_Csv.dropna(how="all")   # Drop all rows with NaN"s

    # filter_Cond cond2 drop columns whose first index of sample no is not V again used to keep only village name
    filter_Cond3 = df_Temp1["Sample No."].str[0] == "V"
    df_Temp1.where(filter_Cond3, inplace=True)
    df_Temp1 = df_Temp1.dropna(how="all")   # Drop all rows with Nan"s
    df_Temp1 = df_Temp1.dropna(1, how="all")  # Drop all cols with Nan"s

    # Create a new column index whose value is that of the index column of DataFrame
    df_Csv["index"] = df_Csv.index
    df_Temp1["index"] = df_Temp1.index

    for cols in df_Csv:  # For each column in DataFrame apply a regex which replaces all chars with blanks
        df_Csv.loc[:, cols].replace(
            regex=True, inplace=True, to_replace=r"[a-zA-Z]", value=r"")

    # Create a list of dictionaries where the column header is the key and the column values are stored in a list ie. value of key
    df_Csv_Dict = df_Csv.to_dict("list")
    df_Temp_Dict = df_Temp1.to_dict("list")

    villages_List = []
    # Create an empty list with key "Village" to add it in the final DataFrame
    df_Csv_Dict["Village"] = villages_List

    # Iterate over village names(second last only)
    for i in range(0, len(df_Temp_Dict["index"])-1):
        for j in range(0, len(df_Csv_Dict["index"])):   # Iterate over samples
            # If index of village name is not present in samples then execute
            if (df_Temp_Dict["index"][i] not in df_Csv_Dict["index"]):
                # Find difference between index number of village 1 and village 2 eg. village1.index = 200 village2.index = 350 then 350-200 = 150;
                for k in range(0, (df_Temp_Dict["index"][i+1] - df_Temp_Dict["index"][i])-1):
                    # execute loop and repeat village name for n times ie. for all samples of that village
                    villages_List.append(df_Temp_Dict["Sample No."][i])
            break    # Once sample found end searching

    # for the last village put here due to index overflow error
    # Find difference between last value of sample and last value of village name
    for i in range(0, (df_Csv_Dict["index"][-1]-df_Temp_Dict["index"][-1])):
        # execute loop and repeat village name for n times ie. for all samples of that village
        villages_List.append(df_Temp_Dict["Sample No."][-1])

    # import the dictionary to DataFrame
    df_Csv = df_Csv.from_dict(df_Csv_Dict)

    cols_Drop = ["Sr.No.", "Sample No.", "EC",
                 "S", "Mn", "Cu", "Zn", "B", "index"]
    df_Csv = df_Csv.drop(cols_Drop, axis=1)  # Drop the above mentioned columns
    # Reorder columns in DataFrame
    df_Csv = df_Csv[["Village", "pH", "N", "P", "K", "OC", "Fe"]]
    df_Csv = df_Csv.dropna()  # Now drop all rows with null values from DataFrame

    # To remove all villages with less than 10 entries
    df_Csv = df_Csv.groupby("Village").filter(lambda x: len(x) >= 10)
    # Reset index to create a final index for DataFrame
    df_Csv = df_Csv.reset_index(drop=True)

    filter_Cond_Letter = string.ascii_letters + ":"
    # filter_Cond out Village: from Village: village_name
    df_Csv["Village"] = df_Csv["Village"].map(
        lambda x: x.lstrip(filter_Cond_Letter))
    # Remove whitespace around village name
    df_Csv["Village"] = df_Csv["Village"].str.strip()
    df_Csv = df_Csv.astype({"pH": "float64", "N": "float64", "P": "float64",
                            "K": "float64", "OC": "float64", "Fe": "float64"})  # Change columns datatype to access as numbers

    df_Temp2 = pd.DataFrame()  # Creating new DataFrame
    village_Names = df_Csv.Village.unique()  # Extract village names
    for i in village_Names:  # To iterate over village list
        # Subsetting main DataFrame village wise
        sub_Csv = df_Csv[df_Csv.Village == i]
        df_Csv_Dict = sub_Csv.to_dict("list")

        for iter in df_Csv_Dict:  # To iterate over each column header
            if iter != "Village":  # If the header is not the Village name
                # Call iqrClean() or z_score_Clean() to remove outliers and put the data back into dictionary
                df_Csv_Dict[iter] = iqrClean(df_Csv_Dict[iter])

        df_Temp2 = df_Temp2.append(df_Temp2.from_dict(
            df_Csv_Dict))  # Append value of df_Csv_Dict to df_Temp1 to create final DataFrame

    # Group final cleaned data by Village and find its mean
    df_Csv = df_Temp2.groupby("Village").mean()
    return df_Csv


def saveFile(save_Path, df_Fin):

    df_Fin.sort_values(by="Village")
    df_Fin.to_csv(save_Path)

    df_Fin.drop(df_Fin.index, inplace=True)
    df_Fin = pd.DataFrame()
    print("Done")


def saveStateFile(side_Path, dir_List, file_List):

    list1 = []

    for i in range(0, len(file_List[0])):
        csv_Path = os.path.join(side_Path, file_List[0][i])
        df_Csv = pd.read_csv(csv_Path)

        df_Csv = df_Csv.mean()
        new_Col = pd.Series([file_List[0][i]], index=["District"])
        df_Csv = df_Csv.append(new_Col)

        list1.append(df_Csv.tolist())

    df_Csv = pd.DataFrame(
        list1, columns=["pH", "N", "P", "K", "OC", "Fe", "District"])
    df_Csv["District"] = df_Csv["District"].str.rstrip(".csv")
    df_Csv = df_Csv[["District", "pH", "N", "P", "K", "OC", "Fe"]]

    df_Csv.to_csv(
        "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Maharashtra Soil.csv", index=False)


if __name__ == "__main__":
    # Path to import file
    start = time.time()
    main_Path = "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Soil/"
    dir_List, file_List = dirNames(main_Path)

    makePath(main_Path, dir_List, file_List)

    side_Path = "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Final soil_Village/"
    dir_List, file_List = dirNames(side_Path)

    saveStateFile(side_Path, dir_List, file_List)

    end = time.time()
    print(f"Total Execution Time = {end-start}")
