
#!/bin/sh

#This code runs on EC2 Spark Master instance

spark-submit <name of the pyspark program specific to use case that you wish to implement, below is sample code for wordcount>
# Push output of above program to S3 data lake using below code

aws s3 cp buyerdata.csv s3://commerce-datalake

#Invoke SSH to Ubuntu (Seller machine) for Kafka producer job
HOST='<IP address of Ubuntu machine which is generated due to OpenVpn, you can find it from ifconfig command e.g. 10.8.0.3'
    USER='<name of the Ubuntu machine here'
    PORT='22'
    PASSWORD='password of the user on Ubuntu machine'
    sshpass -p $PASSWORD ssh -p $PORT $USER@$HOST sh  <Enter File path on Ubuntu machine where you have saved program1.sh>
