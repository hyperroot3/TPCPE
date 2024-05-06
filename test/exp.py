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


def matrix_size(elements_kinds, reactants_terms, products_terms):
    rows_user = len(elements_kinds)
    columns_user = len(reactants_terms) + len(products_terms)
    return rows_user, columns_user


def generate_zero_matrix(rows, columns):
    row_echelon = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        row_echelon.append(row)
    return row_echelon


def fill_matrix(parsed_reactants, parsed_products, unique_elements, zero_matrix):

    for i, reactant in parsed_reactants:
        for element, count in reactant.items():
            zero_matrix[unique_elements.index(element)][i] = -count

    for i, product in parsed_products:
        for element, count in product.items():
            zero_matrix[unique_elements.index(element)][i + len(parsed_reactants)] = count
    return zero_matrix



def main():

    equation_user = input("Enter chemical equation: ")
    parsed_reactants_user, parsed_products_user, unique_elements_user = parse_equation(equation_user)
    reactant_counts = count_atoms(parsed_reactants_user)
    product_counts = count_atoms(parsed_products_user)

    matrix_size_user = matrix_size(unique_elements_user, parsed_reactants_user, parsed_products_user)
    zero_matrix = generate_zero_matrix(matrix_size_user[0], matrix_size_user[1])

    print(zero_matrix)

    print("Elements:", unique_elements_user)
    print("\nReactant Atom Counts:", reactant_counts)
    print("Product Atom Counts:", product_counts)
    print(parsed_products_user)

if __name__ == "__main__":
    main()
