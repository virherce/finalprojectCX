def initial_cover(universe, subsets):
    uncovered = set(universe)
    cover = []
    used_sets = set()

    # count how many sets each element appears in
    element_frequency = {}
    for subset in subsets:
        for element in subset:
            if element in element_frequency:
                element_frequency[element] += 1
            else:
                element_frequency[element] = 1

    while uncovered:
        best_set = None
        best_score = -1

        for i, subset in enumerate(subsets):
            if i in used_sets:
                continue

            score = 0
            for element in subset:
                if element in uncovered:
                    score += 1 / element_frequency[element]

            if score > best_score:
                best_score = score
                best_set = i

        if best_set is None:
            break

        cover.append(subsets[best_set])
        used_sets.add(best_set)
        uncovered -= set(subsets[best_set])

    return cover

def is_valid_cover(cover, universe):
    covered = set()
    for subset in cover:
        covered.update(subset)
    return covered == set(universe)

def generate_neighbors(current_cover, all_subsets, universe):
    neighbors = []
    for i in range(len(current_cover)):
        # try removing one set from the current cover
        new_cover = current_cover[:i] + current_cover[i+1:]
        if is_valid_cover(new_cover, universe):
            neighbors.append(new_cover)
    return neighbors

def hill_climb_set_cover(universe, all_subsets):
    current_cover = initial_cover(universe, all_subsets)
    improved = True

    while improved:
        improved = False
        neighbors = generate_neighbors(current_cover, all_subsets, universe)

        for neighbor in neighbors:
            if len(neighbor) < len(current_cover):
                current_cover = neighbor
                improved = True
                break  # move to first better neighbor

    return current_cover

U = [1, 2, 3, 4]
S = [
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 4]
]

optimized_cover = hill_climb_set_cover(U, S)
print(optimized_cover)