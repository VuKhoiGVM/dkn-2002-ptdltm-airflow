from airflow.decorators import task, dag
from airflow.providers.docker.operators.docker import DockerOperator

from datetime import datetime 

@dag(start_date=datetime(2021, 1, 1), schedule_interval='@daily', catchup=False)
def docker_dag():
    
    @task()
    def t1():
        pass
    
    t2 = DockerOperator(
        task_id = 't2',
        image='stock_image:v1.1.0',
        command='python3 stock_data.py',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
        
    )
    
    t1() >> t2 

dag = docker_dag()