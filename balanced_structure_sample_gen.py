#
# sample generator, for N nodes
# A balanced Sample:
# create node names 1 to N
# pick a mix ratio of group A to B of between .2 to .5
# generate following edges
# every combo pair from A
# every combo pair in B
# every combo of 1 from A and 1 from B
# shuffle them and output sample

# do above but change 1 ++ to -- or 1 -- to ++ in sample
import random
import itertools

names = [s.strip() for s in open('10000names.txt', 'r').readlines()]  # base 10,000 names


def gen_edges(n, balanced=True, randomize=True, numbers=False):
    global names

    if n > 10000:
        print('*** sample limited to 10000 names ***')

    if numbers:
        sample = [str(i) for i in range(1,n+1)]
    else:
        sample = random.sample(names, n)

    i = int(random.randrange(int(n/4), int(n/4*3)))
    group_a = sample[:i]
    group_b = sample[i:]

    a_edges = itertools.combinations(group_a, 2)
    b_edges = itertools.combinations(group_b, 2)

    cross_edges = itertools.product(group_a, group_b)

    edges = [f'{n1} ++ {n2}' for n1, n2 in a_edges]
    edges.extend([f'{n1} ++ {n2}' for n1, n2 in b_edges])
    edges.extend([f'{n1} -- {n2}' for n1, n2 in cross_edges])

    if not balanced:  # change one sign
        print("BALANCED:\n")
        i = random.randrange(len(edges))
        if '++' in edges[i]:
            edges[i].replace('++', '--')
        else:
            edges[i].replace('--', '++')
    else:
        print("NOT BALANCED:\n")


    if randomize:
        random.shuffle(edges)
    print(n, len(edges))
    for l in edges:
        print(l)

gen_edges(10,balanced=False, numbers=False, )