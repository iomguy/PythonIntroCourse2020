import time
import numpy as np

py_list = [i for i in range(10000)]
start = time.process_time()
py_list_2 = [i+1 for i in py_list]
end = time.process_time()
print("list:", round(end-start, 5))

py_arr = np.array(py_list)
start = time.process_time()
py_arr += 1
end = time.process_time()

print("NumPy array:", round(end-start, 5))