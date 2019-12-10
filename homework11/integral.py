import math

h_list = [0.5, 1]
x1 = -2
x2 = 2

def y(x):
    return math.sqrt(16 - x * x)

def integra_y(x):
    return 0.5 * x * math.sqrt(16  - x ** 2) + 8 * math.asin(x/4)

def middle_rect(h):
    k = int((x2 - x1) / h)
    t = 0
    for i in range(k):
        t += y((x1 + i * h + x1 + (i + 1) * h) / 2)
    return h * t 

def trapezoid(h):
    k = int((x2 - x1) / h)
    t = 0
    for i in range(k + 1):
        if i == 0 or i == k:
            t += y(x1 + i * h) / 2
        else:
            t += y(x1 + i * h)
    return h * t

def simson(h):
    k = int((x2 - x1) / h)
    t = 0
    for i in range(k + 1):
        x = x1 + i * h
        if i == 0 or i == k:
            t += y(x)
        elif i % 2 == 1:
            t += 4 * y(x)
        else:
            t += 2 * y(x)
    return h * t / 3

for h in h_list:
    rect = middle_rect(h)
    tra = trapezoid(h)
    sim = simson(h)
    real = integra_y(x2) - integra_y(x1)
    print('--------Шаг:', h)
    print('middle_rect:', rect, 'precison:', abs(real - rect))
    print('trapezoid:', tra, 'precison:', abs(real - tra))
    print('simson:', sim, 'precison:', abs(real - sim))

# --------Шаг: 0.5
# middle_rect:  15.317782947920461  precison: 0.011999308072169868
# trapezoid:    5.281760363921013   precison: 0.02402327592727893
# simson:       15.30565771604382   precison: 0.00012592380447173923
# --------Шаг: 1
# middle_rect:  15.353452420289436  precison: 0.04766878044114442
# trapezoid:    15.210068307552588  precison: 0.09571533229570406
# simson:       15.304023333311617  precison: 0.0017603065366742499
