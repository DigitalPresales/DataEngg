cd <enter path where this code is resided on Ubuntu(seller machine)
python3 python.py

#kafka producer here 
cd /opt/kafka/bin/
sh kafka-console-producer.sh --topic logstopic < /<some file path where you wish to store output file>/o1.csv --bootstrap-server localhost:9092
