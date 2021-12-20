import random
def estimate_pi(n):
    num_points_circle = 0
    num_points_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            num_points_circle += 1 #If distance <=1 (mean that point stay inside the circle) : we increase n_circle plus 1
        num_points_total +=1 #Whatever distance <=1 or >1 (mean that point stay outside the circle but inside the square) : we also increase n_total plus 1
    return 4*num_points_circle/num_points_total

print (estimate_pi(10000000))