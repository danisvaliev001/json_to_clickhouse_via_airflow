# json_to_clickhouse_via_airflow
This project reproduces an example of using airflow to put raw data from the JSON file to ClickHouse. The result is data ready for analytics work.

## How to use:
1. At the command prompt, change directory, create raw directory and start docker-compose:  
`cd *path*`  
`mkdir raw`  
`docker-compose up -d`  

2. Open web-interface in browser:  
http://localhost:8080/admin/  

3. Start scheduler:  

![start_scheduler](https://imgur.com/a/7UY7Vj3)  
