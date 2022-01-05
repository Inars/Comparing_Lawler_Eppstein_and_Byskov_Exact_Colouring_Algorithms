import math
import random
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="results")

parser.add_argument('-v', '--vertices', help='choose the number of vertices', default=4, type=int)
parser.add_argument('-e', '--edges', help='choose the number of edges', default=4, type=int)
parser.add_argument('-alg', '--algorithm', help='choose between lawler, eppstein, and byskov', default='lawler', type=str)
parser.add_argument('-data', '--dataset', help='choose a file path', default=None, type=str)

class Algorithm():

    def __init__(self, args):

        self.args = args
        self.V = []
        self.v = 0
        self.E = []
        self.e = 0

        if args.dataset != None:
            self.V, self.v, self.E, self.e = self.load_graph(args.dataset)
        else:
            self.v, self.e = args.vertices, args.edges
            self.V, self.E = self.generate_graph(self.v, self.e)
        self.G = [self.V, self.E]

        self.x = 0
        if args.algorithm == 'lawler':
            self.x = self.lawler(self.G)
        if args.algorithm == 'eppstein':
            self.x = self.eppstein(self.G)
        if args.algorithm == 'byskov':
            self.x = self.byskov(self.G)


    def load_graph(self, filename):

        print('Loading graph from ./data/{}\n'.format(filename))

        f = open('./data/'+filename, 'r')

        v = int(f.readline())
        V = []
        for i in range(v):
            V.append(int(f.readline()))
        
        e = int(f.readline())
        E = []
        for i in range(e):
            edges = f.readline().split()
            E.append([int(edges[0]),int(edges[1])])

        return V, v, E, e

    def generate_graph(self, v, e):

        print('Generating graph...')

        V, E = [], []

        f = open('./data/graph.data', 'w')
        f.write(str(v)+'\n')
        for i in range(v):
            V.append(i)
            f.write(str(i)+'\n')
        f.write(str(e)+'\n')
        for i in range(e):
            vertex1 = 0
            vertex2 = 0
            while vertex1 == vertex2:
                vertex1 = random.randint(0,v-1)
                vertex2 = random.randint(0,v-1)
                for i in range(len(E)):
                    if len(np.setdiff1d([vertex1,vertex2],E[i])) == 0:
                        vertex1 = 0
                        vertex2 = 0
            E.append([vertex1,vertex2])
            f.write(str(vertex1)+' '+str(vertex2)+'\n')
        f.close()

        print('Graph generated to ./data/graph.data')

        return V, E

    def powerset(self, S):
        x = len(S)
        masks = [1 << i for i in range(x)]
        for i in range(1 << x):
            yield [s for mask, s in zip(masks, S) if i & mask]

    def mis(self, S, E):
        A = [] # this will equal S along with truth value of consideration of each element
        B = [] # this will equal all the elements Ei that exclusively have elements from A 
        I = []
        s = list(self.powerset(S))
        
        for i in range(len(S)):
            A.append([S[i], True]) # this means: "for every element S[i] do we still consider it?"
        for i in range(len(E)):
            for j in range(len(s)):
                if len(s[j])!=2:
                    continue
                if len(np.setdiff1d(E[i], [s[0],s[1]]))==0:
                    B.append([E[i][0], E[i][1], True]) 
        
        print(A,B)
        for i in range(len(A)):
            if A[i][1] == True:
                I.append(A[i][0]) # A[i][0] is equal to S[i]
                A[i][1] = False
                for j in range(len(B)):
                    if B[j][2] == True:
                        elements_to_remove = np.setdiff1d([B[j][0],B[j][1]],A[i][0])
                        if len(elements_to_remove)<2:
                            B[j][2] = False
                            for k in range(len(elements_to_remove)):
                                A[S.index(elements_to_remove[k])][1] = False
                                for l in range(len(B)):
                                    if B[l][2] == True:
                                        if len(np.setdiff1d([B[l][0],B[l][1]],elements_to_remove[k]))<2:
                                            B[l][2] = False
                                            #print(B)

        return I
        
    
    def lawler(self, G):
        X = np.zeros(2**len(G[0]), dtype=np.int)
        S = list(self.powerset(G[0]))
        for i in range(len(S)):
            X[i] = len(S[i])
            I = self.mis(S[i],G[1])
            print(I,S[i])


    def eppstein(self, G):
        pass

    def byskov(self, G):
        pass

if __name__ == '__main__':

    args = parser.parse_args()
    print('Algorithm : {}\n'.format(args.algorithm))

    alg = Algorithm(args)