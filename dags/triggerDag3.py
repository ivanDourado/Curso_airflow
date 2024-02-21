from airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG('triggerdag3', description="trigger",
           schedule_interval=None, start_date=datetime(2024,2,1),
           catchup=False)

task1 = BashOperator(task_id='tsk1', bash_command='exit 1',dag=dag)
task2 = BashOperator(task_id='tsk2', bash_command='exit 1',dag=dag)
task3 = BashOperator(task_id='tsk3', bash_command='sleep 5',dag=dag,
                     trigger_rule = 'all_failed')# seja executada caso todas falhem

[task1,task2] >> task3