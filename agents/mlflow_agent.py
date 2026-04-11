import mlflow

class MLflowAgent:

    def start_run(self):

        mlflow.start_run()

    def log_metric(self,name,value):

        mlflow.log_metric(name,value)

    def end_run(self):

        mlflow.end_run()