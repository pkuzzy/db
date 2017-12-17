import MySQLdb

def query(opt, db, cursor):
	if opt == 1:
		SQL1 = "SELECT dinstinct, street, count(*) as num from Location group by dinstinct, street"
		SQL2 = "SELECT dinstinct, avg(num) as anum from Strnum group by dinstinct"
		SQL = "SELECT street from ((%s) as Strnum) natural join ((%s) as Avgnum) where num < anum" % (SQL1, SQL2)
		print SQL
		cursor.execute(SQL)
		data = cursor.fetchall()
		return data

def main():
	db = MySQLdb.connect("localhost", "root", "daituo123", "DB")
	cursor = db.cursor()
	print query(1, db, cursor)

if __name__ == '__main__':
	main()