def rela_angle(rela_x, rela_y):
    '''
    Calculate the relative angle from one point to another
    '''
    if rela_x == 0:
        if rela_y >= 0:
            return math.pi / 2
        else:
            return math.pi * 1.5
    init_degree = math.atan(rela_y / rela_x)
    if init_degree > 0:
        if rela_y > 0:
            return init_degree
        elif rela_y < 0:
            return init_degree + math.pi
    elif init_degree < 0:
        if rela_y > 0:
            return init_degree + math.pi
        elif rela_y < 0:
            return init_degree + 2 * math.pi
    else:
        if rela_x > 0:
            return 0
        elif rela_y < 0:
            return math.pi
    return 0
