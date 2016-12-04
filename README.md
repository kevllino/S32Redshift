# S32Redshift
Load HDFS files (Spark) from S3 to Redshift (AWS)

## Context 
Spark jobs results in 1000s of HDFS part files containing all the relevant data of ones analysis. In order to use them the most efficient way, one has to load them in a database, such as Redshift, whill will allow afterwards to integrate the data in a visualisation tool like Qlik. This task consists in: 

<ol>
  <li>creating jsonpath files with the structure of the data that we want to load</li>
  <li>creating manifests with s3 paths to each HDFS file</li>
  <li>loading those files into Redshift with the schema respecting the order defined in the jsonpath</li>
</ol>

## Objective 
Our goal is to automate the above repetitive and time consuming tasks in order to allow data scientists and engineers to spend their valuable time dealing with the analysis of their data. 

## To Run 
