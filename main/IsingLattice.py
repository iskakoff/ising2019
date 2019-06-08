import numpy as np

class IsingLattice:
    def __init__(self, N, J_ij):
        self.N=N
        self.J_ij=J_ij
        self.lattice=np.zeros((N,N), dtype=np.int)
        for i in range(N):
            for j in range(N):
                self.lattice[i,j]=-(-1)**(i+j)


    def spin(self, i,j):
        return self.lattice[i,j]

