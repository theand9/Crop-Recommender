import pandas as pd
import numpy as np


def dataClean(f_Path1, f_Path2):

    df_Cost = pd.read_csv(f_Path1)
    df_MSP = pd.read_csv(f_Path2)

    df_Cost["CROP NAME"].replace(['Arhar', 'Bajra', 'Gram', 'Jowar', 'Maize'
                                  'Sugarcane', 'Urad', 'Wheat', 'Cotton', 'Groundnut', 'Moong(Green gram)', 'Sesamum', 'Soyabean', 'Sunflower', 'Safflower', 'Rapeseed/mustard', 'Rice', 'Niger seed', 'Ragi'], ['Arhar', 'Bajra', 'Gram', 'Jowar', 'Maize', 'Sugarcane', 'Urad', 'Wheat', 'Cotton', 'Groundnut', 'Moong', 'Sesamum', 'Soyabean' 'Sunflower', 'Safflower', 'Mustard', 'Rice', 'Nigerseed', 'Ragi'], inplace=True)
    df_Cost.rename(columns={"CROP NAME": "Crop"}, inplace=True)
    df_Cost = pd.melt(df_Cost, id_vars=[
                      "Crop"], var_name="Year", value_name="Cultivation Cost")

    df_MSP["Crop"].replace(['RICE', 'JOWAR', 'BAJRA', 'MAIZE', 'RAGI', 'WHEAT',
                            'GRAM', 'ARHAR(Tur)', 'MOONG', 'URAD', 'SUGARCANE@', 'COTTON', 'GROUNDNUT IN SHELL',      'RAPESEED/MUSTARD', 'SUNFLOWER SEED', 'SOYABEAN',  'SAFFLOWER', 'SESAMUM', 'NIGERSEED'], ['Rice'      'Jowar', 'Bajra', 'Maize', 'Ragi', 'Wheat', 'Gram', 'Arhar', 'Moong', 'Urad', 'Sugarcane', 'Cotton', 'Groundnut', 'Mustard', 'Sunflower', 'Soyabean',   'Safflower', 'Sesamum', 'Nigerseed'], inplace=True)

    df_MSP = pd.melt(df_MSP, id_vars=["Crop"],
                     var_name="Year", value_name="MSP")
    df_MSP["Year"].replace(['1997', '1998', '1999', '2000', '2001', '2002',
                            '2003', '2004', '2005', '2006', '2007', '2008' '2009', '2010', '2011', '2012', '2013', '2014', '2018-19'], ['1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2019'], inplace=True)
    df_MSP["MSP"] *= 10

    saveFile(df_Cost, df_MSP)


def saveFile(df_Cost, df_MSP):

    df_Cost = df_Cost.sort_values(["Year", "Crop"])
    df_Cost = df_Cost.reset_index(drop=True)

    df_MSP = df_MSP.sort_values(["Year", "Crop"])
    df_MSP = df_MSP.reset_index(drop=True)

    df_Fin = pd.merge(df_MSP, df_Cost, how='left', left_on=[
                      "Crop", "Year"], right_on=["Crop", "Year"])
    df_Fin.to_csv(
        "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Crops/Final Costs.csv", index=False)

    df_Fin.drop(df_Fin.index, inplace=True)
    print("Done")


if __name__ == "__main__":

    path1 = "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Crops/Cultivation cost.csv"
    path2 = "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Crops/MSP.csv"

    dataClean(path1, path2)
