gap = yaw - first_yaw
if gap > 180.0:
    gap -= 360.0
elif gap < -180.0:
    gap += 360.0
