def solution1(lottery):
    from collections import defaultdict
    import math

    answer = -1
    ids = [id[0] for id in lottery]
    result = [r[1] for r in lottery]

    is_won = {}
    result_dict = defaultdict(int)
    for a, b in zip(ids, result):
        if is_won.get(a, False):
            continue

        result_dict[a] += 1
        if b == 1:
            is_won.update({a: True})

    not_won_people = []
    for k, v in result_dict.items():
        if not is_won.get(k):
            not_won_people.append(k)

    for not_won_p in not_won_people:
        del result_dict[not_won_p]

    answer = sum(val for key, val in result_dict.items())
    return math.floor(answer / len(result_dict)) if len(result_dict) != 0 else 0


# print(solution1([[1,0],[35,0],[1,0],[100,1],[35,1],[100,1],[35,0],[1,1],[1,1]]))
# print(solution1([[1,0],[2,0],[3,0]]))


def solution2(grid):
    answer = 0
    return answer


def solution2(grid):
    for row in range(1, len(grid)):
        grid[row][0] = grid[row][0] + grid[row - 1][0]

    for column in range(1, len(grid[0])):
        grid[0][column] = grid[0][column] + grid[0][column - 1]

    for row in range(1, len(grid)):
        for column in range(1, len(grid[0])):
            which_path = []
            which_path.append(grid[row][column] + grid[row - 1][column])
            which_path.append(grid[row][column] + grid[row][column - 1])
            grid[row][column] = min(which_path)

    return grid[-1][-1]


# print(solution2([[1, 8, 3, 2], [7, 4, 6, 5]]))
# print(solution2([[1, 2], [3, 4]]))


def swap_list_value(l, idx1, idx2):
    l[idx1], l[idx2] = l[idx2], l[idx1]
    return l


def solution3(arr, k):
    answer = -1
    count = 1
    while True:
        max_difference_list = []

        for i in arr:
            idx = arr.index(i)
            from_index, to_index = idx - k, idx + k
            from_index = from_index if from_index >= 0 else 0
            to_index = to_index if to_index < len(arr) else len(arr)
            comparison_list = [i-val for val in arr[from_index:to_index]]
            max_difference_list.append(max(comparison_list))
        arr = swap_list_value(
            arr,
            arr.index(
                max(max_difference_list)
            ),
            arr.index(max(max_difference_list))
                + max(max_difference_list)
        )
        print(arr)
        count += 1
        if count == 3:
            break

    return answer


print(solution3([4, 5, 2, 3, 1], k=3))