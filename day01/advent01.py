def read_location_ids(filename):
    left_ids = []
    right_ids = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split()
            if values:
                left_ids.append(int(values[0]))
                right_ids.append(int(values[1]))
    return left_ids, right_ids

def compute_total_distance(left_ids, right_ids):
    sorted_left = sorted(left_ids)
    sorted_right = sorted(right_ids)
    return sum(abs(a - b) for a, b in zip(sorted_left, sorted_right))

def compute_similarity_score(left_ids, right_ids):
    count_right = {num: right_ids.count(num) for num in set(right_ids)}
    return sum(num * count_right.get(num, 0) for num in left_ids)

def main():
    filename = 'advent01.txt'
    left_ids, right_ids = read_location_ids(filename)
    print("Total Distance:", compute_total_distance(left_ids, right_ids))
    print("Similarity Score:", compute_similarity_score(left_ids, right_ids))

if __name__ == "__main__":
    main()