def angle_to_yaw(angle):
    '''
    param: angle      angle is target point related with start point
    param: north      relate the North
    result: change related angle to yaw 
    '''
    if 90.0 >= angle >= 0.0:
        north =  90.0 - angle
    elif 360.0 > angle > 90.0:
        north = 450.0 - angle
    return north
