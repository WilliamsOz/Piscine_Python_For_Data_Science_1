from give_bmi import give_bmi, apply_limit

# height = (2.21)
# height = [1.80]
height = [2.71, 1.15]
# height = [-2.71, -1.15]
# height = ['c', 'c']
# height = [4.42, 'c']
# height = [2.21, 4.42, 8.84]
weight = [165.3, 38.4]
# weight = [86]
# weight = (4.42)
# weight = [2.21, 4.42, 8.84]
# weight = ['c', 'c']
# weight = [4.42, 'c']

bmi = give_bmi(height, weight)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))
# print(apply_limit(bmi, 'c'))
# print(apply_limit(21, 42))
