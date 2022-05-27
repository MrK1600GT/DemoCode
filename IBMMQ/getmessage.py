
import pymqi
#from pymqi import CMQC


queue_manager = 'Queue Manager Name'
channel = 'Channel Name'
host = 'IP Address Host'
port = 'Port'
queue_name = 'Queue Name'
conn_info = '%s(%s)' % (host, port)

#put_opts = pymqi.pmo()
#put_md = pymqi.md()

#put_md['CorrelId'] = b"ABCDEF"

md = pymqi.MD()
md.CorrelId = b"ABCDEF"

gmo = pymqi.GMO()
gmo.Options = pymqi.CMQC.MQGMO_WAIT | pymqi.CMQC.MQGMO_FAIL_IF_QUIESCING
gmo.WaitInterval = -1

qmgr = pymqi.connect(queue_manager, channel, conn_info)

queue = pymqi.Queue(qmgr, queue_name)
message1 = None

try:
    while message1 != 'END':
        message = queue.get(None, md, gmo)
        message1 = message.decode('UTF-8')
        print(message1)
except Exception as e:
    print(e)
queue.close()

qmgr.disconnect()
