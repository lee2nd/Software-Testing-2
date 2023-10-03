def find_matching_pairs(numbers):
    matching_pairs = []

    for i in range(len(numbers)):
        outer_num = numbers[i]

        for j in range(i + 1, len(numbers)):
            inner_num = numbers[j]

            if outer_num % 2 == 0 and inner_num % 2 == 0:
                matching_pairs.append([outer_num, inner_num])
                continue  # Skip to the next iteration of the inner loop

            if outer_num % 2 != 0 and inner_num % 2 != 0:
                break  # Exit the inner loop if both numbers are odd

    return matching_pairs
