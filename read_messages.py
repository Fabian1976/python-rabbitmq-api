from pyrabbit.api import Client
import json

cl = Client('queue01.core.cmc.lan', 'guest', 'guest')

#cl.is_alive()

messages = cl.get_messages('/', 'jenkins_results', requeue=True)

for message in messages:
    payload = json.loads(message['payload'])
#   m = json.loads(message)
#   print '\n' + m['payload']
    print '\nProject    : %s' % payload['project']
    print 'Buildnummer: %s' % payload['number']
    print 'Status     : %s' % payload['status']
    print
