# conversion from logarithmic to linear scale

def db2lin(log):
    linear = 10 * (log / 10)
    return linear