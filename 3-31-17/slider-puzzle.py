# TODO:
    # accept N as a argument to the program

# TODO:
    # create unsolve function
    # create solve function
    #     use A* to solve
    #     heuristic?

import sys
import pdb
import numpy as np
import heapq
import math

# ARGV:
    # 1. N
    # 2. number of moves to unsolve

def unsolve(puzzle, num_moves):
    N = puzzle.shape[0]
    prev_move = -1
    for i in range(num_moves):
        x, y = np.where(puzzle == 0)
        move = np.random.randint(4)
        if move == 0 and prev_move != 0 and x > 0:
            puzzle[x,y], puzzle[x-1,y] = puzzle[x-1,y], puzzle[x,y]
        elif move == 1 and prev_move != 1 and x < (N-1):
            puzzle[x,y], puzzle[x+1,y] = puzzle[x+1,y], puzzle[x,y]
        elif move == 2 and prev_move != 2 and y > 0:
            puzzle[x,y], puzzle[x,y-1] = puzzle[x,y-1], puzzle[x,y]
        elif move == 3 and prev_move != 3 and y < (N-1):
            puzzle[x,y], puzzle[x,y+1] = puzzle[x,y+1], puzzle[x,y]
        prev_move = move
    return puzzle

def not_solved(puzzle, solved_puzzle):
    h = compute_heuristic(puzzle, solved_puzzle)
    if h == 0: return False
    else: return True

def manhatten_distance(puzzle_state):
    count = 1
    mhd = 0
    for i in range(puzzle_state.shape[0] * puzzle_state.shape[1]):
        for j in range(puzzle_state.shape[0]):
            for k in range(puzzle_state.shape[1]):
                if puzzle_state[j,k] == count:
                    xi = j
                    yi = k
                    xbar = int(int(puzzle_state[j,k] - 1) / puzzle_state.shape[0])
                    ybar = int(int(puzzle_state[j,k] - 1) % puzzle_state.shape[1])
                    mhd += math.fabs(xi - xbar) + math.fabs(yi - ybar)

        count += 1
    return mhd

def num_out_of_place(puzzle_state):
    n_out_of_place = 0
    count = 1
    for i in range(puzzle_state.shape[0]):
        for j in range(puzzle_state.shape[1]):
            if puzzle_state[i,j] != count:
                n_out_of_place += 1
            count += 1
    return n_out_of_place

def compute_heuristic(puzzle_state, solved_puzzle):
    # HEURISTIC sum of:
        # - number of tiles out of place
        # - manhatten distance?

    n_out_of_place = num_out_of_place(puzzle_state)
    mhd = manhatten_distance(puzzle_state)
    # difference = np.sum(np.abs(puzzle_state - solved_puzzle))

    return n_out_of_place + mhd

def solve(puzzle, solved_puzzle):
    N = puzzle.shape[0]
    priority_queue = []
    current_depth = 0
    current_heuristic = compute_heuristic(puzzle, solved_puzzle)
    tiebreaker = 0
    heapq.heappush(priority_queue, (current_heuristic, current_depth, tiebreaker, puzzle))
    current_node = heapq.heappop(priority_queue)
    tiebreaker = 0

    while not_solved(current_node[3], solved_puzzle):
        for move in range(4): # NOTE 4 moves
            child_state = current_node[3].copy()
            x, y = np.where(puzzle == 0)
            if move == 0 and x > 0:
                child_state[x,y], child_state[x-1,y] = current_node[3][x-1,y], current_node[3][x,y]
            elif move == 1 and x < (N-1):
                child_state[x,y], child_state[x+1,y] = current_node[3][x+1,y], current_node[3][x,y]
            elif move == 2 and y > 0:
                child_state[x,y], child_state[x,y-1] = current_node[3][x,y-1], current_node[3][x,y]
            elif move == 3 and y < (N-1):
                child_state[x,y], child_state[x,y+1] = current_node[3][x,y+1], current_node[3][x,y]
            h = compute_heuristic(child_state, solved_puzzle)
            print(h)
            current_depth = current_node[1]
            f = h + current_depth
            heapq.heappush(priority_queue, (f, current_depth+1, tiebreaker+1, child_state))
            tiebreaker += 1
        current_node = heapq.heappop(priority_queue)

def main():
    N = int(sys.argv[1])
    num_moves = int(sys.argv[2])
    puzzle = np.zeros((N, N))

    #construct a solved puzzle:
    count = 1
    for i in range(N):
        for j in range(N):
            puzzle[i,j] = count
            count += 1
    puzzle[N-1, N-1] = 0
    solved_puzzle = puzzle.copy()

    puzzle = unsolve(puzzle, num_moves)
    puzzle = solve(puzzle, solved_puzzle)

main()
