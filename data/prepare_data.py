import random
bike = open("bike.csv", "w")
location = open("location.csv","w")

bike.write("bike_id,bike_type,cost_per_min,bike_location\n")
location.write("location_id,dinstinct,street,longitude,latitude\n")

district = ["jiao xue qu", "sheng huo qu"]
street = [["li jiao", "er jiao", "yan nan"], ["xue wu", "yi yuan"]]
lo_r = [[039.990000, 039.992000], [039.988000, 039.989000]]
la_r = [[116.310000, 116.320000], [116.310000, 116.315000]]
dis_r = [[[[0.5, 1], [0.5, 1]], [[0.5, 1], [0, 0.5]], [[0, 0.5], [0, 1]]], [[[0, 1], [0.5, 1]], [[0, 1], [0, 0.5]]]]
# longitude_range = [039.990000, 039.992000]
# latitude_range  = [116.310000, 116.320000]

cnt = 0
for dis in range(len(district)):
	for ss in range(len(street[dis])):
		for i in range(3):
			cnt = cnt + 1
			bike.write("%08d,%02d,%.2f,%08d\n"%(cnt, random.randint(0, 1), random.uniform(0.50, 2.50), cnt))
			lol = (lo_r[dis][1] - lo_r[dis][0]) * dis_r[dis][ss][0][0] + lo_r[dis][0]
			lor = (lo_r[dis][1] - lo_r[dis][0]) * dis_r[dis][ss][0][1] + lo_r[dis][0]
			lal = (la_r[dis][1] - la_r[dis][0]) * dis_r[dis][ss][1][0] + la_r[dis][0]
			lar = (la_r[dis][1] - la_r[dis][0]) * dis_r[dis][ss][1][1] + la_r[dis][0]
			lo = random.uniform(lol, lor)
			la = random.uniform(lal, lar)
			location.write("%08d,%s,%s,%.6f,%.6f\n"%(cnt, district[dis], street[dis][ss], lo, la))

# for dis in district:
# 	for ss in street:
# 		for i in range(2):
# 			cnt = cnt + 1
# 			bike.write("%08d,%02d,%.2f,%08d\n"%(cnt, random.randint(0,10), random.uniform(0.50, 2.50), cnt))
# 			location.write("%08d,0,%s,%s,%.6f,%.6f\n"%(cnt, dis, ss, random.uniform(longitude_range[0],longitude_range[1]), \
# 				random.uniform(latitude_range[0],latitude_range[1])))

bike.close()
location.close()