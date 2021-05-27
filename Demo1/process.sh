  GNU nano 2.9.3                     process.sh                                

#!/bin/sh


echo "Processing product data to sort top brands by rating---"
cd /home/data/airflow/dags/
python3 usecase.py

echo "-------------------------------------------------"

