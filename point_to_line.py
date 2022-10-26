def dist_tree(latitude, longtitude):
    '''
    param: latitude and longtitude
    return: distance of the car to the line
    '''
    XP = GeodeticToCartesian(longtitude, latitude)[1]
    YP = GeodeticToCartesian(longtitude, latitude)[0]
    if dis_flag == 0:
        XA = GeodeticToCartesian(Apoint_longtitude, Apoint_latitude)[1]
        YA = GeodeticToCartesian(Apoint_longtitude, Apoint_latitude)[0]
        XB = GeodeticToCartesian(Bpoint_longtitude, Bpoint_latitude)[1]
        YB = GeodeticToCartesian(Bpoint_longtitude, Bpoint_latitude)[0]
    if dis_flag == 1:
        XA = GeodeticToCartesian(Cpoint_longtitude, Cpoint_latitude)[1]
        YA = GeodeticToCartesian(Cpoint_longtitude, Cpoint_latitude)[0]
        XB = GeodeticToCartesian(Dpoint_longtitude, Dpoint_latitude)[1]
        YB = GeodeticToCartesian(Dpoint_longtitude, Dpoint_latitude)[0]
    if(YA - YB) == 0:
        dist = abs(YP - YA)
    elif(XA - XB) == 0:
        dist = abs(XP - XA)
    else:
        k = (YB - YA) / (XB - XA)
        b = YB - k * XB
        up = abs(k * XP - YP + b)
        down = math.sqrt(k * k + 1)
        dist = up / down
        dist = abs(dist)
    temp = ((YP - b) / k) - XP
    if temp > 0:
        dist = -dist
    else:
        dist = dist
    return dist
