from airflow import DAG 
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import statistics as sts

"""  """

dag = DAG('pythonoperator', description="pythonoperator",
           schedule_interval=None, start_date=datetime(2024,3,5),
           catchup=False)

def data_cleaner():
    dataset = pd.read_csv("/opt/airflow/data/Churn.csv", sep=";")
    dataset.columns = ['Id','Score','Estado','Genero',
                       'Idade','Patrimonio','Saldo','Produtos',
                       'TeamCartCredito','Ativo', 'Salario', 'Saiu'] # nomeia novas colunas
    mediana = sts.median(dataset['Salario'])  # mediana da coluna   
    dataset['Salario'].fillna(mediana, inplace=True) # preenche os campos vazios com os valores da mediana
    dataset['Genero'].fillna('Masculino', inplace=True)# preenche os campos vazios com os valores da mediana

    mediana = sts.median(dataset['Idade'])  # mediana da coluna   
    dataset.loc[(dataset['Idade']<0) | (dataset['Idade']> 120), 'Idade'] = mediana # localiza valores duvidosos (v<0 ou v>120), na coluna Idade e substitui pela mediana

    dataset.drop_duplicates(subset="Id", keep='first',inplace=True)

    dataset.to_csv("/opt/airflow/data/Churn_Clean.csv", sep=";", index = False)

t1 = PythonOperator(
    task_id='t1',
    python_callable=data_cleaner,
    dag=dag
)

t1