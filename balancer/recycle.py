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