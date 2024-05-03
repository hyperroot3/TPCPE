import chemparse as cp


def parse_equation(equation):
    reactants, products = equation.split(' = ')
    parsed_reactants = [cp.parse_formula(formula) for formula in reactants.split(' + ')]
    parsed_products = [cp.parse_formula(formula) for formula in products.split(' + ')]
    unique_elements = identify_elements(parsed_reactants, parsed_products)
    return parsed_reactants, parsed_products, unique_elements


def identify_elements(parsed_reactants, parsed_products):
    unique_elements = set()
    for formula in parsed_reactants + parsed_products:
        unique_elements.update(formula.keys())
    return list(unique_elements)


def count_atoms(parsed_formulas):
    element_counts = {}
    for formula in parsed_formulas:
        for element, count in formula.items():
            element_counts[element] = element_counts.get(element, 0) + count
    return element_counts


def zero_matrix(rows, columns):
    row_echelon = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        row_echelon.append(row)
    return row_echelon

def main():

    equation_user = input("Enter chemical equation: ")
    parsed_reactants_user, parsed_products_user, unique_elements_user = parse_equation(equation_user)
    reactant_counts = count_atoms(parsed_reactants_user)
    product_counts = count_atoms(parsed_products_user)
    print("Elements:", unique_elements_user)
    print("\nReactant Atom Counts:", reactant_counts)
    print("Product Atom Counts:", product_counts)



main()


# Print the output

# print(parsed_reactants)
# print(parsed_products)

rows_user = len(unique_elements_user)
columns_user = len(parsed_reactants_user) + len(parsed_products_user)

print("rows: ", rows_user)
print("columns: ", columns_user)

