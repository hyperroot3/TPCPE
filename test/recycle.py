'''unique_elements = []
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
'''

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
    columns_user = len(reactants_terms) + len(products_terms) + 1
    return rows_user, columns_user


def generate_zero_matrix(rows, columns):
    row_echelon = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        row_echelon.append(row)
    return row_echelon


def gaussian_elimination(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        # Partial pivoting
        max_row = i
        for k in range(i + 1, rows):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Make all elements below this one in the current column zero
        for k in range(i + 1, rows):
            factor = matrix[k][i] / matrix[i][i]
            for j in range(i, cols):
                matrix[k][j] -= factor * matrix[i][j]

    # Back substitution
    for i in range(rows - 1, -1, -1):
        matrix[i][-1] = matrix[i][-1] / matrix[i][i]
        matrix[i][i] = 1
        for k in range(i - 1, -1, -1):
            matrix[k][-1] -= matrix[k][i] * matrix[i][-1]
            matrix[k][i] = 0

    return matrix

