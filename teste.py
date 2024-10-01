



def lerp(P0, P1, t):
    x = (1 - t) * P0[0] + t * P1[0]
    y = (1 - t) * P0[1] + t * P1[1]
    return x, y

A = lerp(P0, P1, t)
