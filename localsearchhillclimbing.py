def build_element_frequency(sets):
    frequency = {}
    for current_set in sets:
        for element in current_set:
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1
    return frequency

def initial_cover(universe_size, sets):
    uncovered = set()
    for i in range(1, universe_size + 1):
        uncovered.add(i)

    cover_indices = []
    used_indices = set()
    frequency = build_element_frequency(sets)

    while len(uncovered) > 0:
        best_score = -1
        best_index = -1

        for i in range(len(sets)):
            index = i + 1
            if index in used_indices:
                continue

            score = 0
            for element in sets[i]:
                if element in uncovered:
                    score += 1 / frequency[element]

            if score > best_score:
                best_score = score
                best_index = index

        if best_index == -1:
            break

        cover_indices.append(best_index)
        used_indices.add(best_index)

        for element in sets[best_index-1]:
            if element in uncovered:
                uncovered.remove(element)

    return sorted(cover_indices)

def is_valid_cover(cover_indices, sets, universe_size):
    covered = set()
    for index in cover_indices:
        for element in sets[index-1]:
            covered.add(element)
    return covered == set(range(1, universe_size + 1))

def generate_neighbors(cover_indices, sets, universe_size):
    neighbors = []
    for i in range(len(cover_indices)):
        new_cover = cover_indices[:i] + cover_indices[i+1:]
        if is_valid_cover(new_cover, sets, universe_size):
            neighbors.append(new_cover)
    return sorted(neighbors)

def hill_climb_set_cover(universe_size, sets):
    current_cover = initial_cover(universe_size, sets)
    print(len(current_cover))
    improved = True

    while improved:
        improved = False
        neighbors = generate_neighbors(current_cover, sets, universe_size)
    
        for neighbor in neighbors:
            if len(neighbor) < len(current_cover):
                current_cover = neighbor
                improved = True
                break
    return sorted(current_cover)

def read_input_file(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()

    first_line = lines[0].strip().split()
    number_of_elements = int(first_line[0])
    number_of_sets = int(first_line[1])

    sets = []
    for line in lines[1:]:
        parts = line.strip().split()
        size = int(parts[0])
        current_set = []
        for i in range(1, size + 1):
            current_set.append(int(parts[i]))
        sets.append(current_set)

    return number_of_elements, number_of_sets, sets

numelems, numsets, sets = read_input_file('small18.in')
print(numelems, numsets, sets)
print(len(hill_climb_set_cover(numelems, sets)))

