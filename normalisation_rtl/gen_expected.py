import numpy as np

# Load data
Q = np.loadtxt('qdata.txt')
K = np.loadtxt('kdata.txt')

# Matrix multiplication: R = Q * K^T
# Note: kdata.txt has K rows, so K^T is needed if we want Q_i * K_j
R = np.dot(Q, K.T)

with open('expected_output.txt', 'w') as f:
    for i, row in enumerate(R):
        abs_sum = np.sum(np.abs(row.astype(int)))
        # Hardware logic: sum_2core = sum[23:7] which is sum // 128
        divisor = int(abs_sum) // 128
        
        f.write("Row {} abs_sum: {} divisor: {}\n".format(i, abs_sum, divisor))
        if divisor == 0:
            norm_row = ["X"] * 8
        else:
            norm_row = [str(int(abs(int(x)) / divisor)) for x in row]
        
        f.write(" ".join(norm_row) + "\n")

print("Generated expected_output.txt")
