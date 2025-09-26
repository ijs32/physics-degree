import numpy as np


def np_eig(A):
    eig_val, eig_vec = np.linalg.eig(A)

    i = np.argmax(np.abs(eig_vec))

    return eig_val[i], eig_vec[:,i]


def power_iterative(A, x, prev_eig, e = 1e-12) -> tuple:

    eig_vec = A @ x
    eig_val = np.linalg.norm(eig_vec)

    if abs(eig_val - prev_eig) < e:
        return eig_val, eig_vec

    x_norm = eig_vec / eig_val

    print(f"x: {x}, eig_val: {eig_val}")
    return power_iterative(A, x_norm, eig_val)


A = np.array([[1,3,5],
              [3,2,9],
              [5,9,5]])
x = np.array([1,0,0])


np_eig_val, np_eig_vec = np_eig(A)
pi_eig_val, pi_eig_vec = power_iterative(A, x, 0)

print(f"np_eig_val: {np_eig_val}, np_eig_vec: {np_eig_vec}")
print(f"pi_eig_val: {pi_eig_val}, pi_eig_vec: {pi_eig_vec}")