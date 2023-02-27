# python3

import sys
import threading

def compute_height(num, nodes):
    EMPTY = -1
    depths = [EMPTY] * num
    for node, parent in enumerate(nodes):
#        print(f"check {node} node with parent {parent}")
        if parent == EMPTY:
            root = node
        if depths[node] != EMPTY:
            continue
        n = node
        p = parent
        depths[n] = 1
        while depths[p] <= depths[n] and p != EMPTY:
#            print(f"depth of {n} with parent {parent}")
            prevDepth = depths[n]
            n = p
            p = nodes[n]
            depths[n]= prevDepth + 1
    return depths[root]
# for every node
# try to go up
# if there is depth calculated, skip
# if there is a bigger depth, don't go up
# if our depth is bigger go up

def main():
    mode = input()
    if "I" in mode:
        num = int(input())
        nodes = list(map(int, input().split()))
    elif "F" in mode:
        fname = input()
        with open("./test/"+fname) as f:
            num = int(f.readline())
            nodes = list(map(int, f.readline().split()))
    else:
        exit()
    print(compute_height(num, nodes))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
