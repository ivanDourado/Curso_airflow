from airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from datetime import datetime


dag = DAG('exemplo_xcom', description="exemplo_xcom",
           schedule_interval=None, start_date=datetime(2024,2,1),
           catchup=False)

def task_write(**kwargs):
    kwargs['ti'].xcom_push(key='valorxcom1', value=10200)

task1 = PythonOperator(
    task_id='tsk1', 
    python_callable=task_write,
    dag=dag
)

def task_read(**kwargs):
    valor = kwargs['ti'].xcom_pull(key='valorxcom1')
    print(f'Valor recuperado: {valor} .')

task2 = PythonOperator(
    task_id='tsk2', 
    python_callable=task_read,
    dag=dag
)    

task1 >> task2
