'''
Problem Statement: 

Calculate the detour distance between two different rides. 
Given four latitude / longitude pairs, where driver one is traveling
from point A to point B and driver two is traveling from point C to point D,
write a function (in your language of choice) to calculate the shorter of the detour
distances the drivers would need to take to pick-up and drop-off the other driver.

'''

''' 
		Author: Mariko Wakabayashi
		Used https://github.com/slawek87/geolocation-python to make calls to the Google Developers API
		to obtain
		-- Info for each (latitude, longitude)
		-- Distance between each point

'''

from geolocation.google_maps import GoogleMaps
from geolocation.distance_matrix import const

google_maps = GoogleMaps(api_key='AIzaSyAF_pJjojJ5kELi7q_W_Kgd6xhfJ7EQ1i0') 

class Point():

	def __init__(self, latitude, longitude):
		self.lat = latitude
		self.lng = longitude

	def __str__(self):
		return '('+str(self.lat)+', '+str(self.long)+')'

	def get_addr(self):
		point = google_maps.search(lat=self.lat, lng=self.lng).first()
		return point.formatted_address

class Route():

	def __init__(self, point1, point2):
		self.start = google_maps.search(lat=point1.lat, lng=point1.lng).first()
		self.end = google_maps.search(lat=point2.lat, lng=point2.lng).first()
		origin = [self.start.formatted_address]
		destination = [self.end.formatted_address]
		self.dist_info = google_maps.distance(origin, destination).first()
		
	def get_distance(self, unit='miles'):
		if unit == 'kilometers':
			return self.dist_info.distance.kilometers
		elif unit == 'meters':
			return self.dist_info.distance.meters
		else:
			return self.dist_info.distance.miles

def input_lat_lng(point):
	'''Gathers input from user and converts them to Points
		Input must have two float numbers seperated by white space'''

	num = raw_input('Enter latitude and longitude for '+point+' (must be a float): ').split(' ')

	try:
		lat_lng = map(float, num)
		return Point(lat_lng[0], lat_lng[1])
	except ValueError:
		return input_lat_lng(point)

def difference(dist1, dist2):
	return dist1 - dist2

def shortestDetour(A, B, C, D, unit="miles"):
	'''Find the shorter of the detour distance 
		 Define detour distance as the distance to pick up, drop off the driver, and reach own destination point.
		 Two options to take: A -> C -> D ->B or C -> A -> B -> D
		 Since the distance from A -> C + D -> B == C -> A + B -> D,
		 we will determine the shortest detour distance by comparing 
		 the distance between A -> B and C -> D'''
	AB = Route(A, B)
	CD = Route(C, D)
	AC = Route(A, C)
	DB = Route(D, B)

	AB_dist = AB.get_distance(unit)
	CD_dist = CD.get_distance(unit)
	AC_dist = AC.get_distance(unit)
	DB_dist = DB.get_distance(unit)

	detour_dist = AC_dist + DB_dist
	diff = difference(AB_dist, CD_dist)
	# If distance AB is greater or equal, we will choose route ACDB. 
	if AB_dist >= CD_dist:
		detour_dist += CD_dist
		return 'A: {0} -> \nC: {1} -> \nD: {2} -> \nB: {3}'.format(A.get_addr(), C.get_addr(), D.get_addr(), B.get_addr()), \
		'\nShortest detour: {0} {1}'.format(detour_dist, unit), \
		'\nDifference between the longer detour: {0} {1}'.format(diff, unit)

	# else route CABD
	else:
		detour_dist += AB_dist
		return 'C: {0} -> \nA: {1} -> \nB: {2} -> \nD: {3}'.format(C.get_addr(), A.get_addr(), B.get_addr(), D.get_addr()), \
		'\nShortest detour: {0} {1}'.format(detour_dist, unit), \
		'\nDifference between the longer detour: {0} {1}'.format(abs(diff), unit)

def main():
	#gather input from user
	A = input_lat_lng('A')
	B = input_lat_lng('B')
	C = input_lat_lng('C')
	D = input_lat_lng('D')

	route, dist, diff = shortestDetour(A, B, C, D)

	print route, dist, diff
if __name__ == "__main__":
    
    main()

#### EXAMPLES For testing ####
# Example 1
	# lyft_office = '37.760339 -122.412672'
	# stanford_campus = '37.428264 -122.168845'
	# SFO = '37.621313 -122.378955'
	# apple_hq = '37.332112 -122.030776'
	# Enter latitude and longitude for A (must be a float): 37.760339 -122.412672
	# Enter latitude and longitude for B (must be a float): 37.428264 -122.168845
	# Enter latitude and longitude for C (must be a float): 37.621313 -122.378955
	# Enter latitude and longitude for D (must be a float): 37.332112 -122.030776
	# A: Mission District, San Francisco, CA, USA -> 
	# C: 173 Airport Access Rd, San Francisco, CA 94128, USA -> 
	# D: Cupertino, CA 95014, USA -> 
	# B: Serra Mall @ Lasuen Mall, Stanford, CA 94305, USA 
	# Shortest detour: 57.6009 miles 
	# Difference between the longer detour: 0.0622 miles
	
# Example 2
	# newyork = '40.7127 -74.0059'
	# sanfrancisco = '37.7833 -122.4167'
	# miami = '25.7753 -80.2089'
	# lasvegas = '36.1215 -115.1739'
	
	# Enter latitude and longitude for A (must be a float): 40.7127 -74.0059
	# Enter latitude and longitude for B (must be a float): 37.7833 -122.4167
	# Enter latitude and longitude for C (must be a float): 25.7753 -80.2089
	# Enter latitude and longitude for D (must be a float): 36.1215 -115.1739
	# A: Manhattan, New York, NY, USA -> 
	# C: East Little Havana, Miami, FL, USA -> 
	# D: Paradise, NV, USA -> 
	# B: Eddy St & Hyde St, San Francisco, CA 94102, USA 
	# Shortest detour: 4377.5517 miles 
	# Difference between the longer detour: 377.7929
