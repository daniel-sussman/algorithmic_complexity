def quick_sort(l):
    if len(l) < 2:
        return l
    else:
        pivot = l[0]
        left = []
        right = []
        for i in l[1:]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [pivot] + quick_sort(right)