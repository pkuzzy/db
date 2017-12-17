'''
	bike.py
	Bike Part:
		insert(ID, info) (ok/exist)
		delete(ID) (ok/not_exist)
		query(ID) (ok info/not_exist)
'''

import MySQLdb

def insert(ID, info, db, cursor):
	SQL = "SELECT * from Bike where bike_id = '%d'" % (ID)
	cursor.execute(SQL)
	data = cursor.fetchone()
	if data != None:
		return 'exist'
	SQL = "INSERT INTO Location (loc_id, dinstinct, street, longitude, latitude) VALUES ('%d', '%s', '%s', '%g', '%g')"\
			% (ID, info[2], info[3], float(info[4]), float(info[5]))	
	# print SQL
	cursor.execute(SQL)
	db.commit()
	SQL = "INSERT INTO Bike (bike_id, bike_type, cost_per_min, bike_location) VALUES ('%d', '%d', '%g', '%d')" \
			% (ID, int(info[0]), float(info[1]), ID)
	cursor.execute(SQL)
	db.commit()
	return 'ok'

def delete(ID, db, cursor):
	SQL = "SELECT * from Bike where bike_id = '%d'" % (ID)
	cursor.execute(SQL)
	data = cursor.fetchone()
	if data == None:
		return 'not_exist'
	SQL = "DELETE from Bike where bike_id = '%d'" % (ID)
	cursor.execute(SQL)
	db.commit()
	SQL = "DELETE from Location where loc_id = '%d'" % (ID)
	cursor.execute(SQL)
	db.commit()
	return 'ok'

def query(ID, db, cursor):
	SQL = "SELECT * from Bike where bike_id = '%d'" % (ID)
	cursor.execute(SQL)
	data = cursor.fetchone()
	if data == None:
		return 'not_exist'
	bike_type = int(data[1])
	cost_per_min = float(data[2])
	SQL = "SELECT * from Location where loc_id = '%d'" % (ID)
	cursor.execute(SQL)
	data = cursor.fetchone()
	dinstinct = data[1]
	street = data[2]
	longitude = float(data[3])
	latitude = float(data[4])
	return 'ok', bike_type, cost_per_min, dinstinct, street, longitude, latitude

def nearby(dinstinct, street, db, cursor):
	SQL = "SELECT bike_id from Bike, Location where bike_id = loc_id and dinstinct = '%s' and street = '%s'" \
			% (dinstinct, street)
	cursor.execute(SQL)
	data = cursor.fetchall()
	print data
	res = ''
	for bike in data:
		res += str(bike[0]) + ' '
	return res

def main():
	db = MySQLdb.connect("localhost", "root", "daituo123", "DB")
	cursor = db.cursor()
	# print delete(1, db, cursor)
	print insert(5, [1, 1.1, 'shenghuo', 'dajie', 100, 200], db, cursor)
	print query(2, db, cursor)
	print nearby('shenghuo', 'dajie', db, cursor)
	# print delete(1, db, cursor)


if __name__ == "__main__":
	main()


