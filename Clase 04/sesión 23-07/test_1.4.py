
"""Decoradores en Python"""
import time


def mesureTime(func):

    def calculator(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Tiempo de ejecución es: {}".format(time.time() - start))

        return result
    return calculator


@mesureTime
def suma(a, b, c, d):
    time.sleep(1)
    return a + b + c + d


@mesureTime
def resta(x, y):
    time.sleep(1)
    return x - y


print(suma(90, 500, 600, 1000))
print(resta(90, 500))
# 1.0143084526062012
# 1.0049798488616943
# 1.000143051147461

# 1.0099730491638184
# 1.008418083190918
# 1.005486249923706
