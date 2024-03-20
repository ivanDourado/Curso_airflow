from airflow import DAG 
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.providers.http.sensors.http import HttpSensor
import requests

"""  """

dag = DAG('httpsensor', description="httpsensor",
           schedule_interval=None, start_date=datetime(2024,3,15),
           catchup=False)

def query_api(): # função que realiza requisição
    response = requests.get('https://api.publicapis.org/entries') # metódo q consulta API
    print(response.text) # printa retorno da API

check_api = HttpSensor(
    task_id= 'check_api', # id 
    http_conn_id ='connection', # nome da conexão que cadastramos na UI 
    endpoint='entries', # enpoint da API
    poke_interval=5, # intervalo entre tentativas
    timeout=20, # espera
    dag=dag # dag
)

process_data = PythonOperator( # operador python o qual chama a função query_api
    task_id = 'process_data',
    python_callable=query_api, # chama função
    dag=dag
)

check_api >> process_data