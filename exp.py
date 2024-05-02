# Importing chemparse module
import chemparse

# Ask user input
equation = input("Enter chemical equation: ")
reactants, products = equation.split(' = ')

# Split the equation into molecules
parsed_reactants = [chemparse.parse_formula(formula) for formula in reactants.split(' + ')]
parsed_products = [chemparse.parse_formula(formula) for formula in products.split(' + ')]

unique_elements = []
for formula in parsed_reactants + parsed_products:
    for element in formula.keys():
        if element not in unique_elements:
            unique_elements.append(element)

reactant_counts = {}
for formula in parsed_reactants:
    for element, count in formula.items():
        reactant_counts[element] = reactant_counts.get(element, 0) + count

product_counts = {}
for formula in parsed_products:
    for element, count in formula.items():
        product_counts[element] = product_counts.get(element, 0) + count

# Print the output
print("Elements:", unique_elements)
print("\nReactant Atom Counts:", reactant_counts)
print("Product Atom Counts:", product_counts)

#print(parsed_reactants)
#print(parsed_products)

rows = len(unique_elements)
columns = len(parsed_reactants) + len(parsed_products)

print("rows: ", rows)
print("columns: ", columns)

print()
