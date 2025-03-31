from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


def provide_model_results(preds, values):
    quality_parameters = {
        'TP': 0,
        'TN': 0,
        'FP': 0,
        'FN': 0
    }
    i = 0
    for prediction in preds:
        match prediction, values[i]:
            case (0, 0):
                quality_parameters['TP'] += 1
            case (0, 1):
                quality_parameters['FP'] += 1
            case (1, 0):
                quality_parameters['FN'] += 1
            case (1, 1):
                quality_parameters['TN'] += 1
        i += 1
    return quality_parameters


def precision(params):
    TP, FP = params['TP'], params['FP']
    return TP/(TP + FP)


def recall(params):
    TP, FN = params['TP'], params['FN']
    return TP/(TP + FN)


def f1_score(params):
    prec, rec = precision(params), recall(params)
    return (2*prec*rec)/(prec + rec)


def data_train_test_split(X_in, Y_in, train_size, random_state):
    test_size = 1. - train_size
    X_train, X_test, Y_train, Y_test = train_test_split(X_in, Y_in, train_size=train_size, test_size=test_size,
                                                        shuffle=True, random_state=random_state)
    return X_train, X_test, Y_train, Y_test


def vectorize_series(series):
    vector = []
    for item in series:
        vector.append(item)
    return vector


def transform_data(df):
    in_data = []
    out_data = []
    for item in df.iterrows():
        vectorized_data = vectorize_series(item[1])
        feature_vector = vectorized_data[:-1]
        out_value = int(vectorized_data[-1])
        in_data.append(feature_vector)
        out_data.append(out_value)
    return np.array(in_data), np.array(out_data)


def prepare_data():
    apps_data = pd.read_csv("../raw_data/apps_data_complete.csv")
    X, Y = transform_data(apps_data)
    X_train, X_test, Y_train, Y_test = data_train_test_split(X, Y, 0.80, 17)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, Y_train, Y_test


def append_result_to_file(content, path):
    with open(path, 'a') as file:
        content = content + "\n"
        file.write(content)


def create_file(name):
    path = f"./data/{name}"
    with open(path, "a") as file:
        return path


