import pandas as pd
import numpy as np
import keras.layers
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras import models
from keras.layers import Dense, Activation, Flatten
from keras.utils.vis_utils import plot_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from itertools import chain
import matplotlib.pyplot as plt
import pickle
from ann_visualizer.visualize import ann_viz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


def loadData(f_Path):
    df_Fin = pd.read_csv(f_Path)

    pph = df_Fin["Min PPH"]
    df_Fin.drop(["Min PPH"], axis=1, inplace=True)

    X = df_Fin.to_numpy(copy=True)
    y = pph.to_numpy(copy=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=145)

    return X_train, X_test, y_train, y_test


def NNModel(X_train):
    model = Sequential()

    # Input Layer
    model.add(Dense(64, kernel_initializer="normal",
                    input_dim=X_train.shape[1]))
    model.add(keras.layers.ELU(alpha=1.0))

    # # Hidden Layers

    model.add(Dense(128, kernel_initializer="normal"))
    model.add(keras.layers.ELU(alpha=1.0))

    model.add(Dense(128, kernel_initializer="normal"))
    model.add(keras.layers.ELU(alpha=1.0))

    model.add(Dense(256, kernel_initializer="normal"))
    model.add(keras.layers.ELU(alpha=1.0))

    model.add(Dense(256, kernel_initializer="normal"))
    model.add(keras.layers.ELU(alpha=1.0))

    # Output Layer
    model.add(Dense(1, kernel_initializer="normal", activation='linear'))

    model.compile(loss="mean_absolute_error", optimizer="adam",
                  metrics=["mae"])
    model.summary()

    # plot_model(model, to_file='C:/Users/amogh/Desktop/model_plot.png',
    #            show_shapes=True, show_layer_names=True, rankdir="LR")
    # ann_viz(model, view = True, filename = "C:/Users/amogh/Desktop/model_plot1", title="Predictive Yield Neural Network")

    return model


def trainModel(model, X_train, X_test, y_train, y_test):
    filepath = "C:/Users/amogh/Desktop/weights_best.hdf5"
    checkpoint = ModelCheckpoint(
        filepath, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]

    trained_Model = model.fit(X_train, y_train, validation_data=(
        X_test, y_test), epochs=300, batch_size=15, callbacks=callbacks_list)
    model_Viz(trained_Model)

    pkl_filename = "pickle_model.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(model, file)


def model_Viz(history):
    # Plot training & validation loss values
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()


if __name__ == "__main__":
    path = "C:/Users/amogh/Desktop/SBMP/6th sem/Final Year Project/Dataset/Crops/train_data2.csv"

    X_train, X_test, y_train, y_test = loadData(path)
    weight_Path = "C:/Users/amogh/Desktop/weights_best.hdf5"

    model = NNModel(X_train)
    model.load_weights(weight_Path)
    trainModel(model, X_train, X_test, y_train, y_test)
