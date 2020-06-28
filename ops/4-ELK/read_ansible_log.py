import socket
import json
import os 
import sys 
import re 

if len(sys.argv) != 2:
    print('Useage:', sys.argv[0], 'ansible_log_path')
    sys.exit(1)


if not os.path.exists(sys.argv[1]):
    print('file', sys.argv[1], 'not exsits')
    sys.exit(1)

s = socket.socket()
s.connect(('192.168.1.249', 12345))

r = re.compile(r'(?P<time>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}).*\su=(?P<user>.*)\s\|\s\s(?P<host>.*)\s\|\s(?P<status>.*)\s=>.*')


for line in open(sys.argv[1]).readlines():
    result = re.finditer(r, line)    
    items = [m.groupdict() for m in result]
    if not items:
        continue
    s.send((json.dumps(items[0])+'\r\n').encode('utf-8'))
s.close()





[2020-06-19T07:45:33,145][WARN ][logstash.outputs.elasticsearch][main] Attempted to resurrect connection to dead ES instance, but got an error. {:url=>"http://172.19.0.2:9200/", :error_type=>LogStash::Outputs::ElasticSearch::HttpClient::Pool::HostUnreachableError, :error=>"Elasticsearch Unreachable: [http://172.19.0.2:9200/][Manticore::ConnectTimeout] connect timed out"}