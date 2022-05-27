# encoding: utf-8

import pymqi
from pymqi import CMQC


queue_manager = 'Queue Manager Name'
channel = 'Channel Name'
host = 'IP Address Host'
port = 'Port'
queue_name = 'Queue Name'
message = 'Das ist eine Testnachricht'
conn_info = '%s(%s)' % (host, port)

put_opts = pymqi.pmo()
put_md = pymqi.md()

put_md['CorrelId'] = b"ABCDEF"
put_md['Persistence'] = CMQC.MQPER_PERSISTENT
bytes_encoding = 'utf-8'
#bytes_encoding = 'iso-8859-1'
default_ccsid = 1208

qmgr = pymqi.connect(queue_manager, channel, conn_info, bytes_encoding=bytes_encoding, default_ccsid=default_ccsid)

queue = pymqi.Queue(qmgr, queue_name)

for i in range(1, 11):
    message = 'Das ist die {}. Nachricht.'.format(i)
    queue.put(message, put_md, put_opts)
    print(message)

message = 'END'
queue.put(message, put_md, put_opts)

queue.close()

qmgr.disconnect()