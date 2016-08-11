def main():
    E, v = input_data()
    if not check_v_for_parity(int(v), E):
        print('NONE')
        return
    paths = []
    while sum([1 for link in E if not link.used]) > 0:
        current_top = search_not_used_link(E)
        current_path = [current_top, ]
        paths.append(fill_path(current_path, current_top, E))
    while len(paths)>1:
        paths = merge_paths(paths)
    print(" ".join(paths[0]))


def merge_paths(paths):
    for i in range(len(paths)):
        for j in range(len(paths)):
            same_top = get_same_top(paths[i], paths[j])
            if i != j and same_top:
                i = paths[i]
                j = paths[j]
                jj = [j[(j.index(same_top)+1+k)%len(j)] for k in range(len(j)-1)]
                ii = i[:(i.index(same_top)+1)] + jj + i[(i.index(same_top)):]
                paths.remove(j)
                paths.remove(i)
                paths.append(ii)
                return paths


def get_same_top(path1, path2):
    for i in path1:
        for j in path2:
            if i == j:
                return i
    return None


def fill_path(current_path, current_top, E):
    for link in E:
        if current_top in link.e and not link.used:
            link.used = True
            current_top = link.get_another_top_from_link(current_top)
            if current_path[0] == current_top:
                return current_path
            current_path.append(current_top)
    return fill_path(current_path, current_top, E)


def check_v_for_parity(count_v, E):
    dict_v = {}
    for i in range(1, count_v+1):
        dict_v[i] = sum([1 for link in E if str(i) in link.e])
        if dict_v[i] % 2 == 1 or dict_v[i] == 0:
            return False
    return True


def search_not_used_link(E):
    for link in E:
        if not link.used:
            return link.e[0]
    return None


def input_data():
    v, e = input().split()
    E = []
    for i in range(int(e)):
        E.append(Link(input().split()))
    return E, v


class Link:
    def __init__(self, e):
        self.e = e
        self.used = False

    def get_another_top_from_link(self, top):
        return self.e[self.e.index(top)-1]


main()
