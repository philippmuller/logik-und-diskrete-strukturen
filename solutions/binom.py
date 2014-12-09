import scipy.special as sp

first = (sp.binom(4,1) * sp.binom(48,4)) / (sp.binom(52,5))
first_2 = 1 - ((sp.binom(44,4) + sp.binom(3,1) * sp.binom(44,3)) / (sp.binom(47,4)))
second = (sp.binom(4,2) * sp.binom(12,3) * sp.binom(4,1)**3) / (sp.binom(52,5))
second_2 = 1 - (sp.binom(45,3) / sp.binom(47,3))
third = (sp.binom(4,3) * sp.binom(12,2) * sp.binom(4,1)**2) / (sp.binom(52,5))
third_2 = (sp.binom(12,1) * sp.binom(4,1)**2) / (sp.binom(47,2))
forth = (sp.binom(4,4) * sp.binom(12,1) * sp.binom(4,1)) / (sp.binom(52,5))
forth_2 = (sp.binom(12,1)) / (sp.binom(47,1))

result = first*first_2 + second*second_2 + third*third_2 + forth*forth_2

print(result)


# print(first)
# print(second*13)
# print(third*13)
# print(forth*13)

# print("Trilling: \n")
# print(third)
# print((54912/2598960)/13)

# check 4
