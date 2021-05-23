
#!/bin/sh

#This code runs on EC2 Spark Master instance

spark-submit <name of the pyspark program specific to use case that you wish to implement, below is sample code for wordcount>
# Push output of above program to S3 data lake using below code

aws s3 cp aws s3 cp <Output file generated from program above> s3://commerce-datalake s3://commerce-datalake

#Invoke SSH to Ubuntu (Seller machine) for Kafka producer job
HOST='<IP address of Ubuntu machine which is generated due to OpenVpn, you can find it from ifconfig command e.g. 10.8.0.3'
    USER='<name of the Ubuntu machine here'
    PORT='22'
    PASSWORD='password of the user on Ubuntu machine'
    sshpass -p $PASSWORD ssh -p $PORT $USER@$HOST sh  <Enter File path on Ubuntu machine where you have saved program1.sh>
    
    
#--------------------------- Sample wordcount program for Spark -------------------------#
from  pyspark import SparkContext
from  pyspark import SparkConf
import subprocess # Use this if you wish to invoke or call any shell script

if __name__ == "__main__":

#  sc = SparkContext("local","MYAPP")
#  sc.setLogLevel("ERROR")
 
  conf = SparkConf().setAppName("PySpark App").setMaster("Enter name of the addreess from admin URL generated on EC2 master which is Public DNS name and :8080 e.g. spark://ubuntu:7077")
  sc = SparkContext(conf=conf)


  lines = sc.textFile("Enter file path of test data or data feed here")
  words =  lines.flatMap(lambda line: line.split(" "))
  
  subprocess.call("shell script name e.g. /home/data/test.sh", shell=True)  # Use this if you wish to invoke or call any shell script

  wordCounts = words.countByValue()
  for word, count in wordCounts.items():
     print("{}: {}".format(word, count))


