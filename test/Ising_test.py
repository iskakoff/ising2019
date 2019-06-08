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


if __name__ == '__main__':
    unittest.main()
