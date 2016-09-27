# define a function for the interpolate formula
def interpolate(a, b, t):
    return a + t * (b - a)

x = interpolate(10, 24, 0.5)

print x
