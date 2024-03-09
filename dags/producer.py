from airflow import DAG, Dataset
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd


"""  """

dag = DAG('producer', description="producer",
           schedule_interval=None, start_date=datetime(2024,3,5),
           catchup=False)

mydataset = Dataset("/opt/airflow/data/Churn_new.csv")

#função que copia o data set renomeando-o
def my_file():
    dataset = pd.read_csv("/opt/airflow/data/Churn.csv", sep=";") # lê
    dataset.to_csv("/opt/airflow/data/Churn_new.csv", sep=";") # copia renomeando

# task q executa função my_file
t1= PythonOperator(
    task_id='t1',
    python_callable = my_file,
    dag=dag,
    outlets = [mydataset] # avisa q a task atualizará o dataset
)