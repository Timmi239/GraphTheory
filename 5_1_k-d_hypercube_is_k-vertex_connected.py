# Докажите, что k-мерный гиперкуб k-связен с помощью теоремы Менгера.
#
# k-мерным гиперкубом называется граф, в котором вершины — битовые строки длины k,
# а рёбра проведены между теми парами вершин, которые отличаются ровно в одном бите.
# На вход подаётся две различные битовых строки A и B длины k<100 через пробел.
# Выведите k простых путей в k-мерном гиперкубе из A в B, не пересекающихся по внутренним вершинам.
# Формат вывода: один путь на строку; путь – последовательности битовых строк, разделённая пробелами.


def main():
    top_start, top_finish = input().split()
    # top_start, top_finish = '00000', '10101'

    tops_set = {top_start, top_finish}

    paths = extend_paths_by_another_step([top_start], len(top_start))
    while any([True for path in paths if path[-1] != top_finish]):
        for i in range(len(paths)):
            if paths[i][-1] != top_finish:
                paths[i], tops_set = reduce_diff(paths[i], top_finish, tops_set)
    output_list(paths)


def extend_paths_by_another_step(current_path, length):
    paths = []
    for i in range(length):
        neighbor_top = _get_neighbor_top(current_path[-1], i)
        paths.append(current_path + [neighbor_top])
    return paths


def reduce_diff(current_path, top_finish, tops_set):
    for i in get_diff(current_path[-1], top_finish):
        neighbor_top = _get_neighbor_top(current_path[-1], i)
        if neighbor_top not in tops_set or neighbor_top == top_finish:
            tops_set.add(neighbor_top)
            return current_path + [neighbor_top], tops_set
    for i in get_same(current_path[-1], top_finish):
        neighbor_top = _get_neighbor_top(current_path[-1], i)
        if neighbor_top not in tops_set or neighbor_top == top_finish:
            tops_set.add(neighbor_top)
            return current_path + [neighbor_top], tops_set
    return current_path[:-1], tops_set


def _get_neighbor_top(current_top, place):
    changed_bit = '0' if current_top[place] == '1' else '1'
    return ''.join(current_top[:place] + changed_bit + current_top[place+1:])


def get_diff(current_top, top_finish):
    return [i for i in range(len(current_top)) if current_top[i] != top_finish[i]]


def get_same(current_top, top_finish):
    return [i for i in range(len(current_top)) if current_top[i] == top_finish]


def output_list(result_list):
    for item in result_list:
        print(' '.join(item))


if __name__ == '__main__':
    main()


# Sample Input 1:
# 1010 0010
# Sample Output 1:
# 1010 0010
# 1010 1011 0011 0010
# 1010 1000 0000 0010
# 1010 1110 0110 0010
#
# Sample Input 2:
# 0 1
# Sample Output 2:
# 0 1
