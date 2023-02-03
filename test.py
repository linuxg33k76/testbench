
from geopy import distance

user_feet = 32

center_point = [{'lat': -7.7940023, 'lng': 110.300000}]
test_point = [{'lat': -7.7940023, 'lng': 110.300100}]
radius = user_feet # in feet

center_point_tuple = tuple(center_point[0].values())
test_point_tuple = tuple(test_point[0].values())

dis = distance.great_circle(center_point_tuple, test_point_tuple).feet #WGS 84 Earth Radius
print(f'Distance: {dis:0.2f} ft')

if dis <= radius:
    print("{} point is inside the {} ft radius from {} coordinate".format(test_point_tuple, user_feet, center_point_tuple))
else:
    print("{} point is outside the {} ft radius from {} coordinate".format(test_point_tuple, user_feet, center_point_tuple))