# dkn-2002-ptdltm-airflow

set up environment:
docker-compose up 

## Simple datapipeline

### Step:

1. config DAG
2. create connection to HTTP
3. create operator to get API
4. use XCom to extract data
5. store data to database

### file: user_processing.py

### dag: user_processing

### command to check data in database:

1. docker exec -it material-2_postgres_1 /bin/bash
2. psql -Uairflow
3. SELECT * FROM users;

## Scheduling Dag depend on Dataset trigger

### Step:

1. define Dataset
2. define producer to update Dataset
3. define consumer which schedule parameter was Dataset from producer

### file: producer.py; consumer.py

### dag: producer; consumer

### check Dataset trigger in:

1. DAGs view -> Trigger column -> Dataset update
2. Dataset view

## Parallel task

**Using CeleryExecutor**

### Step:

1. define Dag
2. define task with parallel

### file: parallel_dag.py

### dag: parallel_dag

### command and step to run Parallel Task:

1. docker-compose down && docker-compose --profile flower up -d
2. Check Flower UI on: localhost:5555
3. add new worker in airflow-compose
4. check worker available in Flower UI: click on worker -> queue -> name
5. check task send to new queue when trigger Dag

## Group task

### Step:

1. create group folder to define group of Operator Dowload and Transform
2. define group_dag.py with config task from call function from group folder which is pre-defined

### file: group_dag.py

### dag: group_dag

### check group dag is avalable:

1. navigate to graph view in dag -> have button can group task in 1 task

## XCom task and specific path rule for data pipeline

### Step:

1. create task with push and pull data to XCom
2. config trigger rule
3. write dag

### file: xcom_dag.py

### dag: xcom_dag

### check XCom dag data:

1. go to XCom view in Admin -> Check value column

## Elastic Plugins

### Step:

1. Config Elastic Search in local:
    1. dowload docker-compose-es.yaml
    2. docker-compose -f docker-compose-es.yaml up -d
    3. docker-compose -f docker-compose-es.yaml p
    4. go to localhost:9200 to check elastic search was avalable in docker or check in command line:
        1. docker exec -it material-2_elastic_1 /bin/bash
        2. curl -X GET 'http://elastic:9200'
2. Add elastic_hook to plugins system
    1. config elastic_hook.py in plugins folder
    2. in command line:
       1. docker exec -it material-2_airflow-scheduler_1 /bin/bash
       2. airflow plugins
       3. add AirflowElasticPlugin
    3. down and up docker-compose to restart -> check airflow plugins again
3. add elastic_hook in elastic_dag

### file: elastic_dag.py, plugins/hooks/elastic/elastic_hook.py

### dag: elastic_dag
