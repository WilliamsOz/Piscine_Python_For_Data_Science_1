from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

family2 = [[1.80, 78.4],
           [2.15, 102.7],
           [2.10, 98.5],
           [1.88, 75.2],
           [1.80, 78.4],
           [2.15, 102.7],
           [2.10, 98.5],
           [1.88, 75.2]]

# slice_me(family, 0, 10)

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
# print(slice_me(family, 0, 5))
# print(slice_me(family, 1, -2))
# print(slice_me(family, 4, 10))
