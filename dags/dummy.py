from airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime


dag = DAG('dummy', description="dummy",
           schedule_interval=None, start_date=datetime(2024,2,1),
           catchup=False)

def task_write(**kwargs):
    kwargs['ti'].xcom_push(key='valorxcom1', value=10200)

task1 = BashOperator(task_id='tsk1', bash_command='sleep 1',dag=dag)
task2 = BashOperator(task_id='tsk2', bash_command='sleep 1',dag=dag)
task3 = BashOperator(task_id='tsk3', bash_command='sleep 1',dag=dag)
task4 = BashOperator(task_id='tsk4', bash_command='sleep 1',dag=dag)
task5 = BashOperator(task_id='tsk5', bash_command='sleep 1',dag=dag)

taskdummy = DummyOperator(task_id="taskdummy", dag=dag)

# task dummy não tem função nenhuma, serve para resolver problema de dependência
[task1,task2,task3] >> taskdummy >>  [task4,task5]