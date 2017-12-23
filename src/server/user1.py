'''
	user.py
	User part:
		login(username, password) (wrong/admin/user)
		register(username, password) (ok/exist)
		zhanghu(username) (username, admin/user/, rest_money)
		delete(username) (ok/not_exist)
		charge(username, money) (rest_money)
'''

import MySQLdb

def login(username, password, db, cursor):
	SQL = "SELECT * from User where usr_name = '%s'" % (username)
	cursor.execute(SQL)
	data = cursor.fetchone()
	if data == None:
		return "wrong"
	if data[2] == password:
		return data[3]
	return "wrong"

def register(username, gender, career, password, db, cursor):
	SQL = "SELECT * from User where usr_name = '%s'" % (username)
	cursor.execute(SQL)
	data = cursor.fetchone()
	if data != None:
		return "exist" 
	SQL = "INSERT INTO User (usr_name, password, gender, career, usr_type, rmoney) VALUES ('%s', '%s', '%s', '%s', '%s', '%g')" % (username, password, gender, career, 'user', 0)	
	print SQL
	cursor.execute(SQL)
	db.commit()
	return 'ok'

def inform(username, db, cursor):
	SQL = "SELECT * from User where usr_name = '%s'" % (username)
	cursor.execute(SQL)
	data = cursor.fetchone()
	if data == None:
		return None
	return data[1], data[4], data[5], data[3], data[6]

def delete(username, db, cursor):
	SQL = "SELECT * from User where usr_name = '%s'" % (username)
	cursor.execute(SQL)
	data = cursor.fetchone()
	if data == None:
		return 'not_exist'
	else:
		SQL = "DELETE from User where usr_name = '%s'" % (username)
		cursor.execute(SQL)
		db.commit()
		return 'ok'

def charge(username, money, db, cursor):
	SQL = "SELECT rmoney from User where usr_name = '%s'" % (username)
	cursor.execute(SQL)
	data = cursor.fetchone()
	# print data
	rmoney = float(data[0]) + money
	# print rmoney
	SQL = "UPDATE User SET rmoney = '%g' where usr_name = '%s'" % (rmoney, username)
	cursor.execute(SQL)
	db.commit()
	return str(rmoney)

def main():
	db = MySQLdb.connect("localhost", "root", "daituo123", "DB")
	cursor = db.cursor()
	# print register('a', '123', db, cursor)
	# print login('a', '1', db, cursor)
	# print login('a', '123', db, cursor)
	# print login('admin', '123456', db, cursor)
	# print register('a', '123', db, cursor)
	print inform('a', db, cursor)
	# print delete('a', db, cursor)
	print charge('a', 1000, db, cursor)

if __name__ == '__main__':
	main()