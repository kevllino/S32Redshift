from __future__ import print_function
import sys

# specify start and end index of files on the cli, typically blocks of 200/400 files
start = int(sys.argv[1])
end = int(sys.argv[2])
path = str(sys.argv[3])

print('{\"entries\": [',end='\n')
for x in range(start,end):
   print('{"url":"s3://' + path + '/part-%05d", "mandatory":true}'%(x), sep=' ', end='')
   if x < (end - 1):
  	 print(',', sep=' ', end='\n')
print(']}')
