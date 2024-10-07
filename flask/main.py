# from flask import Flask, request, jsonify
# from flask_cors import CORS
import numpy as np

# app = Flask(__name__)
# CORS(app)

HMZ = 200
HDZ = 100
KI = 1
KD_1 = 1.16

K2_i = np.array([1.15, 1.13, 1.11, 1.04, 1.00])
K3_i = np.array([1.15, 1.13, 1.11, 1.04, 1.00])
K5_i = np.array([1.01, 1.03, 1.05])
K4_i = np.array([2.3, 3.5, 3.9])

KM_j = np.array([1.71, 1.00, 0.85, 0.64, 0.40])
KD_j = np.array([1.80, 1.00, 0.89, 0.61, 0.31])

LD_j = np.array([10, 20, 15, 12, 8])
LDC_k = 150

def compute_HM_j(HMZ, KM_j, KI):
    return HMZ * KM_j * KI

def compute_HD_j(HDZ, KD_j, KI):
    return HDZ * KD_j * KI

def compute_Q(LD_j, HD_j, KD_1, K2_i, K3_i):
    return np.sum(LD_j * HD_j * KD_1 * K2_i * K3_i)

def compute_KD4():
    summary_one = np.sum(K4_i * LD_j[:len(K4_i)])
    summary_two = LDC_k * np.sum(LD_j)
    K_D4i = (summary_one + summary_two) / LDC_k
    return K_D4i

HM_j_values = compute_HM_j(HMZ, KM_j, KI)
HD_j_values = compute_HD_j(HDZ, KD_j, KI)
Q = compute_Q(LD_j, HD_j_values, KD_1, K2_i, K3_i)
KD4 = compute_KD4()

print("H_M^j values: ", HM_j_values)
print("H_D^j values: ", HD_j_values)
print("Q values: ", Q)
print("KD4: ", KD4)
# if __name__ == '__main__':
#     app.run(debug=True)