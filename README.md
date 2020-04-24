# json_to_clickhouse_via_airflow
This project reproduces an example of using airflow to put raw data from the JSON file to ClickHouse. The result is data ready for analytics work.

## How to use:
1. Create **raw** directory and put the data-file there called **event-data.json**

1. At the command prompt, start docker-compose:  
`docker-compose up -d`

1. Open web-interface in browser:  
http://localhost:8080/admin/  

1. Start scheduler:  

<img width="1440" alt="airflow_scheduler" src="https://user-images.githubusercontent.com/62111184/80230874-335b7880-865b-11ea-8607-8b70fff59e6a.png">
