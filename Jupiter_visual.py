from random import choice
from math import sqrt

import numpy as np
import matplotlib.pyplot as plt

from pylab import rcParams
rcParams['figure.figsize'] = 10, 10

cluster_radius = 20

class Node():
    ABC = '0123456789ABCDEF'
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.title = ''.join(choice(self.ABC) for x in range(4))
        self.links = []

    def __str__(self):
        return '<%s>' % self.title

    def __repr__(self):
        return self.__str__()

    def add_link(self, neighbor, weight):
        self.links.append({neighbor: weight})


def in_cluster(node1, node2):
    distance = sqrt(pow((node1.x - node2.x), 2) + pow((node1.y - node2.y), 2))
    if distance < cluster_radius:
        return int(distance)
    else:
        return -1
        
def generate_nodes(num=20):
    nodes = []
    for number_of_nodes in range(num):
        x = choice(range(100))
        y = choice(range(100))
        nodes.append(Node(x,y))
    return nodes

def draw_nodes(nodes):
    for node in nodes:
        plt.plot(node.x, node.y, 'ro')
        plt.annotate(node.title, xy=(node.x, node.y), xytext=(node.x, node.y))

def get_links(nodes):        
    for node1 in nodes:
        for node2 in nodes:
            if node1 != node2 and in_cluster(node1, node2) > 0:
                plt.plot([node1.x, node2.x], [node1.y, node2.y])
                node1.add_link(node2, in_cluster(node1, node2))
                    
nodes = generate_nodes()
draw_nodes(nodes)
get_links(nodes)

for node in nodes:
    print('%s: %s' %(node, node.links))

plt.show()
