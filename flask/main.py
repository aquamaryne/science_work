# from flask import Flask, request, jsonify
# from flask_cors import CORS
import numpy as np

# app = Flask(__name__)
# CORS(app)

HMZ = 200
HDZ = 100
KI = 1

KM_j = np.array([1.71, 1.00, 0.85, 0.64, 0.40])
KD_j = np.array([1.80, 1.00, 0.89, 0.61, 0.31])

def compute_HM_j(HMZ, KM_j, KI):
    return HMZ * KM_j * KI

def compute_HD_j(HDZ, KD_j, KI):
    return HDZ * KD_j * KI

HM_j_values = compute_HM_j(HMZ, KM_j, KI)
HD_j_values = compute_HD_j(HDZ, KD_j, KI)

print("H_M^j values: ", HM_j_values)
print("H_D^j values: ", HD_j_values)

# if __name__ == '__main__':
#     app.run(debug=True)