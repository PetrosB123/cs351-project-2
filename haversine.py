import math

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
   radius: int = 3959 # Earth's radius in miles
   lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
   dlat: float = lat2 - lat1
   dlon: float = lon2 - lon1
   # 'a' is the squared half-chord length between the points
   a: float = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
   # 'c' is the angular distance in radians (the central angle)
   c: float = 2 * math.asin(math.sqrt(a))
   return radius * c