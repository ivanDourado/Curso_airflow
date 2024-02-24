from airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'depends_on_past': False,
    'start_date': datetime(2023,2,1),
    'email': ['test@test.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}

dag = DAG('defaultargs', description="Dag de exemplo",
          default_args = default_args,
           schedule_interval=None, start_date=datetime(2024,2,1),
           catchup=False)

task1 = BashOperator(task_id='tsk1', bash_command='sleep 5',dag=dag)
task2 = TriggerDagRunOperator(task_id='tsk2', trigger_dag_id='dagrundag2',dag=dag)

task1 >> task2
