'''

basic chemical bonding balancer

'''
import re
import chemparse as cp

# input

print("Chemical Bonding Balancer\ntype 'help' to see input examples")
print("ex) 2H2 + 4O2 > H2O\n")
# appropriate examples should be made and printed

user_input = str(input('Enter Reactants and Products:'))

reactantsInput = user_input.split('>')[0]
productsInput = user_input.split('>')[1]
# index lists to split reactants / products

print("Reactants:", reactantsInput)
print("Products:", productsInput)

# data processing
reactants = reactantsInput.split('+')
reactants = [i.strip() for i in reactants]

products = productsInput.split('+')
products = [i.strip() for i in products]
# index lists to get individual compounds and remove spaces



print("Reactants:", reactants)
print("Products:", products)


