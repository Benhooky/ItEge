from sklearn.metrics import mean_squared_error
import numpy as np

true_val = np.array([25, 60, 32, 16, 21])
pred_val = np.array([30, 59, 36, 22, 22])

print(mean_squared_error(true_val, pred_val))
