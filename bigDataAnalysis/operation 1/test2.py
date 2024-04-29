import math
def comput(r, h):
    S = 2 * math.pi * r * (r + h)
    V = math.pi * r * r * h
    return S, V
radius = 10
height = 11
result = comput(radius, height)
S, V = result
print("圆柱体的表面积为:", S)
print("圆柱体的体积为:", V)
