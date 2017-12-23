'''
	serve.py
	Main Part
'''

import bike
import order
import user1 as user
import MySQLdb
import search

def sendms(lis):
	if type(lis) == tuple:
		return ' '.join(map(str, lis))
	return lis

def select(s, db, cursor):
	s = s.split()
	if s[0] == 'register':
		res = user.register(s[1], s[2], s[3], s[4], db, cursor)
	if s[0] == 'login':
		res = user.login(s[1], s[2], db, cursor)
	if s[0] == 'dingdan':
		res = order.check(s[1], db, cursor)
		all = ""
		for r in res:
			all += sendms(r) + "\n"
		print all
		return all 
	if s[0] == 'zhanghu':
		res = user.inform(s[1], db, cursor)
	if s[0] == 'zuche':
		res = order.rent(s[1], int(s[2]), db, cursor)
	if s[0] == 'huanche':
		res = order.rent_back(s[1], int(s[2]), db, cursor)
	if s[0] == 'chongzhi':
		res = user.charge(s[1], float(s[2]), db, cursor)
	if s[0] == 'shanchu':
		res = user.delete(s[1], db, cursor)
	if s[0] == 'jiache':
		res = bike.insert(int(s[1]), s[2:], db, cursor)
	if s[0] == 'shanche':
		res = bike.delete(int(s[1]), db, cursor)
	if s[0] == 'chache':
		res = bike.query(int(s[1]), db, cursor)
	if s[0] == 'fujin':
		res = bike.nearby(s[1], s[2], db, cursor)
	if s[0] == 'sousuo':
		res = search.query(int(s[1]), db, cursor)
	print sendms(res)
	return sendms(res)

def main():
	db = MySQLdb.connect("localhost", "root", "daituo123", "DB")
	cursor = db.cursor()
	print select('login a 123', db, cursor)
	# print select('zuche a 1', db, cursor)
	print select('huanche a 10', db, cursor)

if __name__ == "__main__":
	main()