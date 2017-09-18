import sys
import time
import BF
from BF import *
import GUI
from GUI import *
import BT
from BT import *
import FC
from FC import *
import Tkinter
from Tkinter import *

#removes spaces from board
def parser(f):
    s = ''
    fopen = open(f, 'r')
    for line in fopen:
        for i in line:
            if i in '0123456789':
                s = s + i
    fopen.close()
    return s
     
#prints board to console
def printMatrix(s):
    newS = ''
    count = 0
    for i in s:
        count += 1
        newS = newS + i + ' '
        if (count%9 == 0):
            newS += '\n'
    return newS

#generates the test case files
def generate(search_type):
    for i in range(1,6):
        #reset stats
        BFreset()
        BTreset()
        FCreset()
        
        t0 = time.time()
        si = str(i)
        s = parser('puzzle' + si + '.txt')
        if len(s) == 81:
            if (search_type == 'BF'):
                newS = brute_force(s)
                nodes = BF.BFnodes
                search_time = BF.BFTotal

            elif (search_type == 'BT'):
                newS = CSP(s)
                nodes = BT.BTnodes
                search_time = BT.BTTotal

            elif (search_type == 'FC-MRV'):
                newS = FC_MRV(s)
                nodes = FC.FCnodes
                search_time = FC.FCTotal
            else:
                print 'Invalid Search algorithm'
                sys.exit()
            newS = printMatrix(newS)
            fopen = open('solution'+ si +'.txt','w+')
            fopen.write(newS)
            fopen.close()

        t1 = time.time()
        total = t1 - t0

        fopen = open('performance' + si + '.txt','w+')
        s = str(total)
        fopen.write('Total clock time:')
        fopen.write(s)
        fopen.write('\nSearch clock time: ')
        s = str(search_time)
        fopen.write(s)
        fopen.write('\nNumber of nodes generated: ')
        s = str(nodes) + '\n'
        fopen.write(s)
        fopen.close()
      
#writes solutions  
def solution(newS):
        fopen = open('solutions.txt','w+')
        fopen.write(newS)
        fopen.close()

if __name__ == '__main__':
    t0 = time.time()
    if len(sys.argv) == 3:
        s = parser(sys.argv[1])
        if len(s) == 81:
            if (sys.argv[2] == 'BF'):
                    newS = brute_force(s)
                    if (newS == -1):
                        print("Impossible to have a winning configuration for given board")
                        sys.exit()
                    newS = printMatrix(newS)
                    nodes = BF.BFnodes
                    search_time = BF.BFTotal
                    states = BF.BFStates
                    solution(newS)
            elif (sys.argv[2] == 'BT'):
                    newS = CSP(s)
                    if (newS == -1):
                        print("Impossible to have a winning configuration for given board")
                        sys.exit()
                    newS = printMatrix(newS)
                    nodes = BT.BTnodes
                    search_time = BT.BTTotal
                    states = BT.BTStates
                    solution(newS)

            elif (sys.argv[2] == 'FC-MRV'):
                    newS = FC_MRV(s)
                    if (newS == -1):
                        print("Impossible to have a winning configuration for given board")
                        sys.exit()
                    newS = printMatrix(newS)
                    nodes = FC.FCnodes
                    search_time = FC.FCTotal
                    states = FC.FCStates
                    solution(newS)
    else:
        print 'Usage: SudokuSolver.py'   
    
    print newS
    t1 = time.time()
    total = t1 - t0

    fopen = open('performance.txt','w+')
    s = str(total)
    fopen.write('Total clock time:')
    fopen.write(s)
    fopen.write('\nSearch clock time: ')
    s = str(search_time)
    fopen.write(s)
    fopen.write('\nNumber of nodes generated: ')
    s = str(nodes) + '\n'
    fopen.write(s)
    fopen.close()

    #GUI bonus
    display_GUI(states)

    print 'Total clock time:', total
    print 'Search clock time: ', search_time
    print 'Number of nodes generated: ', nodes
    generate(sys.argv[2])
