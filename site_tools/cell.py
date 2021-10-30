from geographiclib.geodesic import Geodesic
from shapely.geometry import Point, Polygon


def createCell(longitude, latitude, azimuth, **kwargs):
    """
    :param longitude: double. 
    :param latitude: double. 
    :param azimuth: int.  
    :param beam: int, default '30'. 
    :param radius: int, default '3'. Unit KM, only valid for wgs84 espg4236
    :param resolusi: int, default '3'. resolusi busur nya.
    
    :return: Polygon. Cell sector polygon geometry.
    """

    beam = kwargs.get('beam',30)
    radius = kwargs.get('radius',3)*10**3
    resolusi = kwargs.get('resolusi',3)
    geod = Geodesic.WGS84

    points = list()

    start_angle = (azimuth - abs(beam)/2) % 360
    end_angle = (start_angle + beam) % 360

    if start_angle > end_angle:
        start_angle -= 360.0

    points.append(Point(longitude, latitude))
    while start_angle < end_angle:
        busur = geod.Direct(latitude, longitude, start_angle, radius, Geodesic.LATITUDE | Geodesic.LONGITUDE)
        points.append(Point(busur['lon2'], busur['lat2']))
        start_angle += resolusi

    busur = geod.Direct(latitude, longitude, end_angle, radius, Geodesic.LATITUDE | Geodesic.LONGITUDE)
    points.append(Point(busur['lon2'], busur['lat2']))
    return Polygon([[p.x, p.y] for p in points])