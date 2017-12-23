'''
	main.py
	Main Part of serve:
'''

import serve
import MySQLdb
import socket

def main():
	db = MySQLdb.connect("localhost", "root", "daituo123", "DB")
	cursor = db.cursor()
	s = socket.socket()
	host = socket.gethostname()
	port = 30011
	s.bind((host, port))
	s.listen(10)
	while True:
		# print "waiting connect!"
		c, addr = s.accept()
		str = c.recv(1024)
		print str
		res = serve.select(str, db, cursor)
		c.sendall(res)
		c.close()

if __name__ == "__main__":
	main()