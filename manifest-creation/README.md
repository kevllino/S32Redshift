## Context 
The scripts genfile.sh and create_manifest.py were implemented to make it easier for users to load data from S3 in AWS Redshift. <br> 

## To run 

./genfile.sh block_size total_number_of_HDFS_parts  bucket/key manifest_name <br>

## Example 

./genfile.sh 500 1000 "bucket1/folder1/folder2" "foo" <br>

Will output 2 manifest files:<br>
foo_manifest_0-500.json <br>
foo_manifest_500-1000.json <br>

They will contain the following lines: <br> 
 
{"entries": [
{"url":"s3://bucket1/folder1/folder2/part-00000", "mandatory":true},
....
{"url":"s3://bucket1/folder1/folder2/part-00999", "mandatory":true},
]}


