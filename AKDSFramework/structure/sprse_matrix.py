# Sparse Matrix for efficient storage

import numpy as np
from AKDSFramework.error import NotValidMatrixError


class SparseMatrix:
    """
    Sparse Matrix representation for efficient storage. Sparse matrix contains less than 30% non
    zero elements. This implementation for sparse matrix uses a dictionary to store values for fast
    access and gives you many wonderful APIs and tools to make your life easy.
    """

    def __init__(self):
        """
        Creates an object of the Sparse Matrix class
        """
        self.matrix = {
            'size': None,
            'elements': {
            }
        }

    def build2D(self, sparse_matrix):
        """
        Build a sparse matrix object from a 2d sparse matrix numpy array. Only Works with 2D Arrays now.
        Args:
            sparse_matrix: 2D Numpy matrix array
        """
        sparse_matrix = np.array(sparse_matrix)
        try:
            row, col = sparse_matrix.shape
            self.matrix['size'] = (row, col)
        except ValueError:
            raise NotValidMatrixError("Your Matrix's some row may have been missing a column")

        for i in range(0, len(sparse_matrix)):
            for j in range(0, len(sparse_matrix[i])):
                if sparse_matrix[i][j] != 0:
                    self.matrix['elements'][f'{[i, j]}'] = sparse_matrix[i][j]

    def get(self, location):
        """
        Remember this get() method only works assuming you given a [a, b] array as SparseMatrix
        currently supports only 2D Arrays
        Args:
            location: Location of where you want to look up the value

        Returns:
            Integer or whatever stored in that place. If nothing then returns zero. Assuming the
            sparse matrix had zero where there was nothing.
        """
        lookup_location = f"[{location[0]}, {location[1]}]"

        try:
            return self.matrix['elements'][lookup_location]
        except KeyError:
            return 0

    def to_numpy(self):
        """
        For whatever reason you want to convert a SparseMatrix object back to a numpy array you can call this
        function.
        Returns:
            Numpy 2D Array equivalent of the SparseMatrix object
        """
        shape = self.matrix['size']
        numpyarray = np.zeros(shape)

        for locations in self.matrix['elements']:
            # Location looks like this [1, 2]
            row = int(locations[1])
            col = int(locations[-2])

            numpyarray[row][col] = self.matrix['elements'][locations]

        return numpyarray

    def shape(self):
        return self.matrix['size']

    def __str__(self):
        return f"{self.matrix}"
