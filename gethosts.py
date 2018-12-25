
#Get ip address of each host in a list

import socket

def get_hosts():
	hosts = ['applegazette.com','socialnewsdaily.com', 'bloggingpro.com']
	
	for h in hosts:

		try:
	
			print("The IP of %s is %s" %(h,socket.gethostbyname(h)))
		
		except socket.error as err_msg:
			print("%s: %s" %(hosts, err_msg))
if __name__ == '__main__':
	get_hosts()

