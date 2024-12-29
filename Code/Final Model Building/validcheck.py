import pandas as pd
import numpy as np
from keras.models import load_model

model_path = "C:/Users/amogh/Desktop/file1.h5"
model = load_model(model_path)


def loadData(f_Path):
    df_Fin = pd.read_csv(f_Path)

    pph = df_Fin["Min PPH"]
    df_Fin.drop(["Min PPH"], axis=1, inplace=True)

    X = df_Fin.to_numpy(copy=True)
    y = pph.to_numpy(copy=True)

    return X, y


def predict(X, y):
    foo = 0
    for i in range(0, len(X)):
        predict_Value = X[i].reshape(1, -1)

        prediction = model.predict(predict_Value)
        foo = abs(prediction - y[i]) + foo

    foo = abs(foo) / len(y)
    print(foo)


if __name__ == "__main__":
    path = "C:/Users/amogh/Desktop/SBMP/6th sem/Project/Dataset/Crops/train_data2.csv"

    X, y = loadData(path)
    predict(X, y)
