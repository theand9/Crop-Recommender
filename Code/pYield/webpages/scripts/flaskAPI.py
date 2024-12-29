import requests
from flask import Flask, request, redirect, url_for, flash, jsonify
import pickle
import numpy as np
import pandas as pd
import json
import tensorflow as tf

app = Flask(__name__)


@app.route('/api/', methods=['GET', 'POST'])
def predictNN():
    data = request.get_json(force=True)
    with graph.as_default():
        prediction = model.predict([np.array(data).reshape(1, -1)])

    return str(prediction)


if __name__ == '__main__':
    modelfile = "C:/Users/amogh/Desktop/SBMP/6th sem/Final Year Project/Code/Final Model Building/pickle_model.pkl"
    model = pickle.load(open(modelfile, 'rb'))

    global graph
    graph = tf.get_default_graph()

    app.run(debug=True, host="127.0.0.1", port=9999)
