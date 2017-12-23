'''
	xml.py
	usage:
		ret_xml(username, location)
		return an xml list
'''
import MySQLdb

def ret_xml(username, location, db, cursor):
	name = [["UserName", username]]
	loc = [["Location", [["District", location[0]], ["Street", location[1]]]]]
	SQL = "SELECT bike_id, order_status from Orders where usr_name = '%s' ORDER BY order_id DESC" % (username)
	cursor.execute(SQL)
	order_info = cursor.fetchone()
	order = [["Order", [["SerialNumber", order_info[0]], ["Status", "Finished"]]]]
	SQL = "SELECT bike_id, bike_type, dinstinct, street, longitude, latitude FROM Bike, Location where bike_location = loc_id AND dinstinct = '%s' AND street = '%s' AND bike_type = 1" % (location[0],location[1])
	cursor.execute(SQL)
	bike_info = cursor.fetchall()
	bike = []
	for B in bike_info:
		S = ["Bike", [["SerialNumber", B[0]], ["Type", B[1]], ["Location", [["District", B[2]], ["Street", B[3]], ["Longitude", B[4]], ["Latitude", B[5]]]]]]
		bike.append(S)
	bike_list = [["BikeList", bike]]
	tot = name + loc + order + bike_list
	doc = [["XML", [["User", tot]]]]
	return list2xml(doc, 0)

def list2xml(doc, lev):
	ret = ""
	tabs = "  " * lev
	for e in doc:
		if type(e[1]) == list:
			ret = ret + tabs + "<%s>\n" % (e[0])
			ret = ret + list2xml(e[1], lev+1)
			ret = ret + tabs + "</%s>\n" % (e[0])
		else:
			ret = ret + tabs + "<%s>" % (e[0])
			if type(e[1]) == long:
				ret = ret + "%d" % (e[1])
			elif type(e[1]) == float:
				ret = ret + "%f" % (e[1])
			else:
				ret = ret + e[1]
			ret = ret + "</%s>\n" % (e[0])
	return ret

def main():
	db = MySQLdb.connect("localhost", "root", "daituo123", "DB")
	cursor = db.cursor()
	print ret_xml('q', ["shenghuoqu", "xuewu"], db, cursor)

if __name__ == "__main__":
	main()
