from data_utils import prepare_data, f1_score, provide_model_results, append_result_to_file, create_file
from sklearn.svm import SVC
import numpy as np
import sys
import time


def run(gamma):
    X_train_scaled, X_test_scaled, Y_train, Y_test = prepare_data()
    min_value = 100
    max_value = 1000
    num_measurements = 35

    log_min = np.log10(min_value)
    log_max = np.log10(max_value)
    log_values = np.linspace(log_min, log_max, num=num_measurements)
    c_values = np.power(10, log_values)[3:]
    file_name = f"rbf_{gamma}.txt"
    path = create_file(file_name)

    for c_value in c_values:
        start_time = time.time()
        model = SVC(kernel="rbf", C=c_value, gamma=gamma)
        model.fit(X_train_scaled, Y_train)
        predictions = model.predict(X_test_scaled)
        results = provide_model_results(predictions, Y_test)
        try:
            score = f1_score(results)
            end_time = time.time()
            execution_time = end_time - start_time
            content = f"score: {score}\tC:{c_value}, gamma: {gamma}, computation_time:{execution_time}s"
        except:
            content = f"fail, div by 0!, results: {results}, C:{c_value}, gamma: {gamma}"
        append_result_to_file(content, path)


if __name__ == "__main__":
    arg = sys.argv[1]
    try:
        result = float(arg)
    except:
        if arg.lower() == "scale":
            result = "scale"
        else:
            result = "auto"
    run(result)