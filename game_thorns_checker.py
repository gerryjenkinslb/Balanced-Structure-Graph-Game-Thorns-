from collections import namedtuple

''' Linear time complete graph check for structural balance checker as per
https://www.reddit.com/r/dailyprogrammer/comments/aqwvxo/20190215_challenge_375_hard_graph_of_thrones/

Algorithm. Since it is a complete graph that has every possible edge between nodes. We don't need a graph.

As we read edges, store edge in dictionary with key as tuple of the two nodes names, 
normalized so the first node in the tuple is less than second

Also as we read in the edges, make a list of all the node names

now just form a path though the node names  n1 ++ n2 -- n3 ++ n4 ++ n5 
and assign them to two groups 1 and 2 based edge value of ++ or --

now for all the rest of edges, just check if any of them are in conflict with the two groups.

'''

Edge = namedtuple('Edge', "n1 n2 friends")


def input_graph(n, m):  # -> dict[(n1,n2)] : Edge, Set() of node names
    edges = {}
    nodes = {}
    for _ in range(m):
        s = input()
        divider = " -- " if " -- " in s else " ++ "
        n1, n2 = s.split(divider)
        if n1 > n2:
            n1, n2 = n2, n1  # normalize
        edges[(n1, n2)] = Edge(n1, n2, divider == ' ++ ')
        if len(nodes) < n:  # collect node names
            nodes[n1] = 0
            nodes[n2] = 0
    return edges, nodes


def bad_edge(nodes, e):
    g1 = nodes[e.n1]
    g2 = nodes[e.n2]
    if e.friends:
        if g1 != g2:
            return True
    else:
        if g1 == g2:
            return True
    return False  # a good edge


def main():
    n, m = map(int, input().split())
    edges, nodes = input_graph(n, m)
    # process path of all nodes to form groups 1 and 2
    keys = iter(nodes.keys())
    from_node = next(keys)
    current_group = 1
    nodes[from_node] = 1  # place first node in group 1
    for n2 in keys:  # rest of path through all nodes
        key = (from_node, n2) if from_node < n2 else (n2, from_node)
        e = edges[key]
        if not e.friends:
            current_group = 3 - current_group # toggle 1>2 2>1
        nodes[n2] = current_group
        from_node = n2
        del edges[key]

    for e in edges.values():
        if bad_edge(nodes, e):
            print("Not Balanced")
            return
    print("Balanced")

if __name__ == '__main__':
    main()