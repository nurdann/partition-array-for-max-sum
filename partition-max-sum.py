def splits(xs, k):
    return [[xs[:i+1], xs[i+1:]] for i in range(min(len(xs), k))]

def part(xs, k):
    if not xs:
        return []
    partitions = []
    for first, rest in splits(xs, k):
        p1 = [max(first)]*len(first) + part(rest, k)
        partitions = partitions + [p1]

    return max(partitions, key=sum)

a = [1,15,7,9,2,5,10]
print(sum(part(a, 3)))
