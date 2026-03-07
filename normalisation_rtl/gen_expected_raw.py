import numpy as np

Q = np.loadtxt('qdata.txt')
K = np.loadtxt('kdata.txt')
R = np.dot(Q, K.T)

with open('expected_output.txt', 'w') as f:
    for row in R:
        abs_sum = np.sum(np.abs(row.astype(int)))
        divisor = int(abs_sum) // 128
        if divisor == 0:
            norm_row = [0] * 8 # Using 0 as a placeholder for undefined/zero-divisor
        else:
            norm_row = [int(x) // divisor for x in row]
        f.write(" ".join(map(str, norm_row)) + "\n")
