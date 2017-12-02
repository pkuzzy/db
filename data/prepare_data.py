import random
bike = open("bike.csv", "w")
location = open("location.csv","w")

bike.write("bike_id,bike_type,cost_per_min,bike_location\n")
location.write("location_id,location_type,district,street,longitude,latitude\n")

district = ["Peking University"]
street = ["li jiao", "er jiao", "yan nan"]
longitude_range = [039.990000, 039.992000]
latitude_range  = [116.310000, 116.320000]

cnt = 0
for dis in district:
	for ss in street:
		for i in range(2):
			cnt = cnt + 1
			bike.write("%08d,%02d,%.2f,%08d\n"%(cnt, random.randint(0,10), random.uniform(0.50, 2.50), cnt))
			location.write("%08d,0,%s,%s,%.6f,%.6f\n"%(cnt, dis, ss, random.uniform(longitude_range[0],longitude_range[1]), \
				random.uniform(latitude_range[0],latitude_range[1])))

bike.close()
location.close()