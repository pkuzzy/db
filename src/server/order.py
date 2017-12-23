'''
	order.py
	Order Part:
		rent(username, bike_id) (ok/used/not_exist/broken/one_bike_only/no_money)
		check(username) (order_list)
		rent_back(username, time) (money)
'''
import MySQLdb

def rent(username, bike_id, db, cursor):
	SQL = "SELECT * from Bike where bike_id = '%d'" % (bike_id)
	cursor.execute(SQL)
	data = cursor.fetchone()
	if data == None:
		return 'not_exist'
	if int(data[2]) == 0:
		return 'broken'
	min_cost = float(data[3])
	SQL = "SELECT * from Orders where bike_id = '%d' AND order_status = '1'" % (bike_id)
	cursor.execute(SQL)
	data = cursor.fetchone()
	if data != None:
		return 'used'
	SQL = "SELECT * from Orders where usr_name = '%s' AND order_status = '1'" % (username)
	cursor.execute(SQL)
	data = cursor.fetchone()
	if data != None:
		return 'one_bike_only'
	SQL = "SELECT * from User where usr_name = '%s'" % (username)
	cursor.execute(SQL)
	data = cursor.fetchone()
	if float(data[6]) < min_cost:
		return "no_money"
	SQL = "INSERT INTO Orders (bike_id, usr_name, order_status) VALUES ('%d', '%s', '1')" \
			% (bike_id, username)
	cursor.execute(SQL)
	db.commit()
	return 'ok'

def check(username, db, cursor):
	SQL = "SELECT * from Orders where usr_name = '%s'" % (username)
	cursor.execute(SQL)
	data = cursor.fetchall()
	return data

def rent_back(username, time, db, cursor):
	SQL = "SELECT * from Orders where usr_name = '%s' AND order_status = '1'" % (username)
	cursor.execute(SQL)
	data = cursor.fetchone()
	bike_id = int(data[1])
	order_id = int(data[0])
	SQL = "SELECT cost_per_min from Bike where bike_id = '%d'" % (bike_id)
	cursor.execute(SQL)
	data = cursor.fetchone()
	cost = float(data[0]) * time
	SQL = "SELECT rmoney from User where usr_name = '%s'" % (username)
	cursor.execute(SQL) 
	data = cursor.fetchone()
	rmoney = float(data[0]) - cost
	SQL = "UPDATE User SET rmoney = '%g' where usr_name = '%s'" % (rmoney, username)
	cursor.execute(SQL)
	db.commit()
	SQL = "UPDATE Orders SET order_status = '0' where order_id = '%d'" % (order_id)
	cursor.execute(SQL)
	db.commit()
	return str(cost)

def main():
	db = MySQLdb.connect("localhost", "root", "daituo123", "DB")
	cursor = db.cursor()
	print rent('a', 1, db, cursor)
	print rent('a', 2, db, cursor)
	print rent('a', 1, db, cursor)
	print check('a', db, cursor)
	print rent_back('a', 20, db, cursor)
	print check('a', db, cursor)

if __name__ == "__main__":
	main()