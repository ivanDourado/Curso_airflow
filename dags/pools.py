from airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

""" Pools são usados para gerenciar a concorrência e a alocação de recursos. 
ex: 
- várias tarefas que precisam acessar um banco de dados. 
- Limites de conexões e recursos;
-você cria um pool que vai limitar e gerenciar o uso destas conexões.  

o que será feito: 
- criar 4 tasks 
- criar 1 pool com 1 slot (worker disponivel para o recurso)
(p pool vai gerenciar o uso do worker)

- definir 'priority_weight para as tasks"""

dag = DAG('pool', description="pool",
           schedule_interval=None, start_date=datetime(2024,3,5),
           catchup=False)

task1 = BashOperator(task_id='tsk1', bash_command='sleep 2',dag=dag, pool="meupool")
task2 = BashOperator(task_id='tsk2', bash_command='sleep 3',dag=dag, pool="meupool", priority_weight=5)
task3 = BashOperator(task_id='tsk3', bash_command='sleep 1',dag=dag, pool="meupool")
task4 = BashOperator(task_id='tsk4', bash_command='sleep 1',dag=dag, pool="meupool", priority_weight=10)



