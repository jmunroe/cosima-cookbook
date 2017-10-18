import cosima_cookbook as cc
from cosima_cookbook.memory import memory

import numpy as np

@memory.cache
def random_matrix(n):
    A = np.random.rand(n, n)
    return A


def test_memory_cache():

    A1 = random_matrix(10)

    A2 = random_matrix(10)

    assert np.equal(A1, A2).all()

