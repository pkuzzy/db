import MySQLdb

def query(opt, db, cursor):
	if opt == 2:
		SQL = "select distinct(street) \
					from (select T.dinstinct, avg(T.num) as anum \
	  						from (select dinstinct, street, count(*) as num \
	        				from Location \
	        				group by street, dinstinct) as T \
	  					group by T.street, T.dinstinct) as D, \
	 					(select dinstinct, street, count(*) as num \
	  						from Location \
	  					group by street, dinstinct) as L \
					where D.dinstinct = L.dinstinct and L.num < D.anum;"
		# print SQL
		cursor.execute(SQL)
		data = cursor.fetchall()
		print data
		return data
	if opt == 1:
		SQL = "select A.usr_name \
				from (select usr_name, count(*) as num \
				from Orders where order_status = 0 group by usr_name) as A \
				where NOT EXISTS \
					(select * from \
						(select usr_name, count(*) as num \
							from Orders where order_status = 0 group by usr_name) as B, \
						(select usr_name, count(*) as num \
							from Orders where order_status = 0 group by usr_name) as C \
					where A.usr_name = B.usr_name and B.num < C.num);"
		cursor.execute(SQL)
		data = cursor.fetchall()
		return data
	# if opt == 3:
	# 	SQL = 	
	if opt == 5:
		SQL = "select B.street \
				from (select dinstinct, street, count(*) as num \
    			from (select bike_id \
      	    		from Bike \
      	   			where bike_type = 0) as BB \
      	    		join Location on BB.bike_id = loc_id \
    				group by dinstinct, street) as B, \
    					(select dinstinct, street, count(*) as num \
    					from (select bike_id \
      	    		from Bike) as TB \
      	    		join Location on TB.bike_id = loc_id \
      				group by dinstinct, street) as T \
				where B.dinstinct = T.dinstinct and B.street = T.street and B.num*2 > T.num;"
		cursor.execute(SQL)
		data = cursor.fetchall()
		return data

def main():
	db = MySQLdb.connect("localhost", "root", "daituo123", "DB")
	cursor = db.cursor()
	print query(2, db, cursor)

if __name__ == '__main__':
	main()