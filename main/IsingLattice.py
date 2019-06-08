import numpy as np

class IsingLattice:
    def __init__(self, N, J_ij, FM=False):
        self.N=N
        self.J_ij=J_ij
        self.lattice=np.zeros((N,N), dtype=np.int)
        for ix in range(N):
            for iy in range(N):
                if FM:
                    self.lattice[ix,iy]=-1
                else:
                    self.lattice[ix,iy]=-(-1)**(ix+iy)


    def spin(self, ix, iy):
        return self.lattice[ix, iy]

    def spin_flip(self, ix, iy):
        self.lattice[ix, iy]=-self.lattice[ix, iy]

    def energy(self):
        E=0
        for I in range(self.N**2):
            ix=I//self.N
            iy=I%self.N
            for J in range(self.N**2):
                jx = J // self.N
                jy = J % self.N
                if abs(ix-jx)==1 and abs(iy-jy)==0:
                    E+=-self.J_ij*0.5*self.lattice[ix,iy]*self.lattice[jx,jy]
                elif abs(ix-jx)==0 and abs(iy-jy)==1:
                    E+=-self.J_ij*0.5*self.lattice[ix,iy]*self.lattice[jx,jy]
                elif abs(ix - jx) == self.N-1 and abs(iy - jy) == 0:
                    E += -self.J_ij * 0.5 * self.lattice[ix, iy] * self.lattice[jx, jy]
                elif abs(ix - jx) == 0 and abs(iy - jy) == self.N-1:
                    E += -self.J_ij * 0.5 * self.lattice[ix, iy] * self.lattice[jx, jy]

        return E



