x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append('{}: {}, {}, {}'.format(*point))
for values in points:
    print(values)

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)
#unzip
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
names, heights = zip(*cast)
print(names)
print(heights)

# transpose with zip
#Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
transpose_data = tuple(zip(*data))
print(transpose_data)