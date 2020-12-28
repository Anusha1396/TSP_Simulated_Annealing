import csv
import os
import sys
import math
import random


def read_file(input_name):
    isEuc = False
    file = []
    with open(input_name, "r") as file:
        file = file.readlines()
        for i in range(len(file)):
            if "EUC_2D" in file[i].strip():
                isEuc = True
            if file[i].strip() == "NODE_COORD_SECTION":
                start = i + 1
            if file[i].strip() == "EOF":
                end = i
    coords = read_coords(file, start, end)

    if isEuc:
        return euc_distance(coords)


def euc_distance(coords):
    # create distance matrix

    length = len(coords)
    distance = [[0 for i in range(length)] for j in range(length)]

    for i in range(length):
        for j in range(length):
            if i == j:
                distance[i][j] = float("inf")

            else:
                distance[i][j] = math.sqrt(
                    ((coords[i][0]) - (coords[j][0])) ** 2 + ((coords[i][1]) - (coords[j][1])) ** 2)

    return distance


def read_coords(file, start, end):
    coords = []
    for i in range(start, end):
        if file[i][0] == ' ':
            file[i] = file[i][1:]
        node_id, x, y = file[i].split()[:3]
        coords.append([int(node_id), float(x), float(y)])
    return coords


def greedy(self):
    cur_node = random.randint(0, self.N - 1)
    solution = [cur_node]

    remain_nodes = set(self.nodes)
    remain_nodes.remove(cur_node)

    while remain_nodes:
        next_node = min(remain_nodes, key=lambda x: self.distance[cur_node][x])
        remain_nodes.remove(next_node)
        solution.append(next_node)
        cur_node = next_node

    cur_total_dis = total_dist(self, solution)
    if cur_total_dis < self.best_dis:
        self.best_dis = cur_total_dis
        self.best_tour = solution
        self.cost_history.append(cur_total_dis)
    return solution, cur_total_dis


def total_dist(self, tour):
    cur_total_dis = 0
    for i in range(self.N):
        cur_total_dis += self.distance[tour[i % self.N]][tour[(i + 1) % self.N]]
    return cur_total_dis


def solution(filename, best_quality, best_tour):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        for val in best_tour:
            writer.writerow([val])


if __name__ == "__main__":
    input_file = sys.argv[1]
    distance = read_file(input_file)
    print(distance[0][1])

