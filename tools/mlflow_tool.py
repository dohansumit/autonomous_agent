import mlflow


def start_run():

    mlflow.start_run()


def log_metric(name,value):

    mlflow.log_metric(name,value)