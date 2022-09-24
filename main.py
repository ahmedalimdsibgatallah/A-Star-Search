from __future__ import annotations

from dataclasses import dataclass
from queue import PriorityQueue

adj = {
    "S": [
        ["A", 1],
        ["B", 4],
    ],
    "A": [
        ["B", 2],
        ["C", 5],
        ["D", 12],
    ],
    "B": [
        ["C", 2],
    ],
    "C": [
        ["D", 3],
    ],
    "D": [],
}

h = {
    "S": 7,
    "A": 6,
    "B": 2,
    "C": 1,
    "D": 0,
}


@dataclass(order=True)
class Node:
    total_cost: int
    actual_cost: int
    node: str
    prev_node: Node


S = Node(node="S", prev_node=None, actual_cost=0, total_cost=0 + h["S"])

minQ = PriorityQueue()
minQ.put(S)

ans = None
while not minQ.empty():
    N = minQ.get()

    if N.node == 'D':
        ans = N
        break

    for node, cost in adj[N.node]:
        new_N = Node(
            node=node,
            prev_node=N,
            actual_cost=N.actual_cost + cost,
            total_cost=N.actual_cost + cost + h[node],
        )

        minQ.put(new_N)


print("Total cost:", ans.actual_cost)

print("Path:")
path = []
curr = ans
while True:
    path.append(curr.node)
    if curr.prev_node is None:
        break;
    curr = curr.prev_node

path.reverse()
for node in path:
    print(node)