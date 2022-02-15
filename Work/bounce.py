# bounce.py
#
# Exercise 1.5

height = 100
bounces = 0


while bounces < 10:
    bounces += 1
    height = height - 0.4 * height
    print(bounces, end = ' ')
    print(round(height, 3))

