import os
from random import random, randint
import mlflow
from mlflow import log_metric, log_param, log_params, log_artifacts


if __name__ == "__main__":
   
    mlflow.set_tracking_uri("http://localhost:6101")

    #log a parameter (key-value pair)
    log_param("config_value", randint(0, 100))

    #log a dictionary of parameters
    log_params({"param1": randint(0, 100), "params2": randint(0, 100)})


    #log a metric can be updated throughout the run
    log_metric("accuracy", random() / 2.0)
    log_metric("accuracy", random() * 0.1)
    log_metric("accuracy", random() + 0.2)

    #log an artifact (output file)
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")
    log_artifacts("outputs")

