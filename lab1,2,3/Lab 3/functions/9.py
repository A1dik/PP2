def sphere_volume(radius):
    a = (4/3) * 3.14 * (radius ** 3) #объем сферы по ее радиусу
    return a
radius = float(input("Radius of the sphere: "))
vol = sphere_volume(radius)
print("Volume of the sphere:", vol)
