from random import choice
from math import sqrt

import numpy as np
import matplotlib.pyplot as plt

ABC = '0123456789ABCDEF'

cluster_radius = 20

class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.title = ''.join(choice(ABC) for x in range(4))

def in_cluster(node1, node2):
    distance = sqrt(pow((node1.x - node2.x), 2) + pow((node1.y - node2.y), 2))
    if distance <= cluster_radius:
        return True
    else:
        return False
        
def generate_nodes(num=25):
    nodes = []
    for number_of_nodes in range(num):
        x = choice(range(100))
        y = choice(range(100))
        nodes.append(Node(x,y))
    return nodes

def draw_nodes(nodes):
    for node in nodes:
        plt.plot(node.x, node.y, 'rx')
        plt.annotate(node.title, xy=(node.x, node.y), xytext=(node.x, node.y))

def get_links(nodes):        
    for node1 in nodes:
        for node2 in nodes:
            if node1 != node2:
                if in_cluster(node1, node2):
                    plt.plot([node1.x, node2.x], [node1.y, node2.y]) 
                    
nodes = generate_nodes()
draw_nodes(nodes)
get_links(nodes)

plt.show()
