def GeodeticToCartesian(longtitude, latitude):
    '''
    Convert GPS coordinates to Gaussian
    The first one returned is the y coordinate
    '''
    Datum = 84
    prjno = 0
    zonewide = 3

    IPI = 0.0174532925199433333333
    lat = latitude
    lon = longtitude

    if(zonewide == 6):
        prjno = math.trunc(lon / zonewide) + 1
        midlon = prjno * zonewide - 3
    else:
        prjno = math.trunc((lon - 1.5) / 3) + 1
        midlon = prjno * 3
    if (Datum == 54):
        a = 6378245
        f = 1 / 298.3
    elif (Datum == 84):
        a = 6378137
        f = 1 / 298.257223563
    midlon = midlon * IPI
    lon = lon * IPI
    lat = latitude * IPI
    e2 = 2 * f - f * f
    L1 = lon - midlon
    t = math.tan(lat)
    m = L1 * math.cos(lat)
    N = a / math.sqrt(1 - e2 * math.sin(lat) * math.sin(lat))
    q2 = e2 / (1 - e2) * math.cos(lat) * math.cos(lat)
    a1 = 1 + 3 / 4 * e2 + 45 / 64 * e2 * e2 + 175 / 256 * e2 * e2 * e2 + 11025 / 16384 * e2 * e2 * e2 * e2 + 43659 / 65536 * e2 * e2 * e2 * e2 * e2
    a2 = 3 / 4 * e2 + 15 / 16 * e2 * e2 + 525 / 512 * e2 * e2 * e2 + 2205 / 2048 * e2 * e2 * e2 * e2 + 72765 / 65536 * e2 * e2 * e2 * e2 * e2
    a3 = 15 / 64 * e2 * e2 + 105 / 256 * e2 * e2 * e2 + 2205 / 4096 * e2 * e2 * e2 * e2 + 10359 / 16384 * e2 * e2 * e2 * e2 * e2
    a4 = 35 / 512 * e2 * e2 * e2 + 315 / 2048 * e2 * e2 * e2 * e2 + 31185 / 13072 * e2 * e2 * e2 * e2 * e2
    b1 = a1 * a * (1 - e2)
    b2 = -1 / 2 * a2 * a * (1 - e2)
    b3 = 1 / 4 * a3 * a * (1 - e2)
    b4 = -1 / 6 * a4 * a * (1 - e2)
    c0 = b1
    c1 = 2 * b2 + 4 * b3 + 6 * b4
    c2 = -(8 * b3 + 32 * b4)
    c3 = 32 * b4
    s = c0 * lat + math.cos(lat) * (c1 * math.sin(lat) + c2 * math.sin(lat) * math.sin(lat) * math.sin(lat) + c3 * math.sin(lat) * math.sin(lat) * math.sin(lat) * math.sin(lat) * math.sin(lat))
    X = s + 1 / 2 * N * t * m * m + 1 / 24 * (5 - t * t + 9 * q2 + 4 * q2 * q2) * N * t * m * m * m * m + 1 / 720 * (61 - 58 * t * t + t * t * t * t)
    Y = N * m + 1 / 6 * (1 - t * t + q2) * N * m * m * m + 1 / 120 * (5 - 18 * t * t + t * t * t * t - 14 * q2 - 58 * q2 * t * t) * N * m * m * m * m * m
    Y = Y + 1000000 * prjno + 500000
    temp = [X, Y]
    return temp
