def load_ratings():
    with open("input.txt", "r") as file:
        ratings = file.read().splitlines()
    
    ratings = [int(rating) for rating in ratings]
    max_rating = max(ratings)
    ratings.extend([0, max_rating + 3])
    ratings.sort()
    return ratings


def diff_nums(ratings):
    diffs = [0, 0, 0] # diffs[0] = num of 1-jolt diffs, and so on...
    
    for index, rating in enumerate(ratings):
        if index == len(ratings) - 1:
            return diffs
        
        next_rating = ratings[index + 1]
        diff = next_rating - rating
        diffs[diff - 1] += 1


def num_of_paths(section):
    total = 0
    start = section[0]
    end = section[-1]
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        
        if path[-1] == end:
            total +=1
            continue
        
        position = path[-1]
        
        for i in [1, 2, 3]:
            if position + i in section:
                path_copy = path.copy()
                path_copy.append(position + i)
                queue.append(path_copy)
    return total


def split_into_sections(ratings):
    sections = []
    current_section_start = 0

    for index, rating in enumerate(ratings):
        if index == len(ratings) - 1:
            return sections
        
        next_rating = ratings[index + 1]
        diff = next_rating - rating
        
        if diff == 3:
            sections.append(ratings[current_section_start: index + 1])
            current_section_start = index + 1


def total_arrangements(ratings):
    total = 1
    sections = split_into_sections(ratings)

    for section in sections:
        num_paths = num_of_paths(section)
        total *= num_paths 
    
    return total


ratings = load_ratings()
diffs = diff_nums(ratings)
print(diffs[0] * diffs[2]) # 2812
print(total_arrangements(ratings)) # 386869246296064
