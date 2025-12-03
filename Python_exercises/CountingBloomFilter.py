import numpy as np

class CountingBloomFilter:
    """
    A counting Bloom filter supporting insert, delete, containment check,
    and approximate element count.

    Attributes:
        size (int): Size of the Bloom filter array.
        k_functions (int): Number of hash functions.
        hash (list): List of hash multipliers.
        counts (numpy array): Counting array storing integer counters.
    """

    def __init__(self, m, k, hash):
        """
        Initializes a Counting Bloom Filter.

        Parameters:
            m (int): Size of the filter.
            k (int): Number of hash functions.
            hash (list[int]): Hash multipliers used for hashing.
        """
        self.size = m
        self.k_functions = k
        self.hash = hash
        self.counts = np.zeros(m, dtype=np.uint8)

    def __hash__(self, x, i):
        """
        Computes the i-th hash function for element x.

        Parameters:
            x (int): Element to hash.
            i (int): Hash function index.

        Returns:
            int: Position in the Bloom filter.
        """
        y = (x * self.hash[i]) % self.size
        return y
    
    def insert(self, x):
        """
        Inserts an element into the counting Bloom filter.

        Parameters:
            x (int): Element to insert.
        """
        for i in range(self.k_functions):
            hash_i = self.__hash__(x, i)
            self.counts[hash_i] += 1
    
    def delete(self, x):
        """
        Removes one occurrence of an element from the filter.

        Parameters:
            x (int): Element to delete.
        """
        for i in range(self.k_functions):
            hash_i = self.__hash__(x, i)
            if self.counts[hash_i] >= 0:
                self.counts[hash_i] -= 1

    def contains(self, x):
        """
        Checks whether an element is possibly in the filter.

        Parameters:
            x (int): Element to check.

        Returns:
            bool: False -> definitely not present, True -> possibly present.
        """
        for i in range(self.k_functions):
            hash_i = self.__hash__(x, i)
            if self.counts[hash_i] == 0:
                return False
        return True
                
    def count(self, x):
        """
        Estimates the count of element x using the minimum counter
        across all hash positions.

        Parameters:
            x (int): Element to count.

        Returns:
            int: Estimated count (∞ if not present).
        """
        final_count = 0
        if self.contains(x):
            final_count = float('inf')
            for i in range(self.k_functions):
                hash_i = self.__hash__(x, i)
                final_count = min(final_count, self.counts[hash_i])
        return final_count
