import unittest

from main.IsingLattice import IsingLattice

class MyTestCase(unittest.TestCase):

    def test_init(self):
        N = 20
        J_ij = 0.5
        ising_lattice = IsingLattice(N, J_ij)
        self.assertEqual(ising_lattice.N, N)
        self.assertEqual(ising_lattice.J_ij, J_ij)

    def test_initial_state(self):
        lattice=IsingLattice(30,.5)
        self.assertEqual(lattice.spin(0,0), -1)
        for i in range(lattice.N):
            for j in range(lattice.N):
                self.assertEqual(lattice.spin(i,j),-(-1)**(i+j))

    def test_spin_flip(self):
        lattice=IsingLattice(30,.5)
        for i in range(lattice.N):
            for j in range(lattice.N):
                s_ij=lattice.spin(i,j)
                lattice.spin_flip(i,j)
                self.assertEqual(lattice.spin(i,j), -s_ij)

    def test_energy(self):
        lattice=IsingLattice(30,.5, True)
        self.assertEqual(lattice.energy(),-lattice.J_ij*2*lattice.N**2)


if __name__ == '__main__':
    unittest.main()
