from time import time
import random
from linear_search import linear_search

random_values =random.sample(range(1000000),1000000)
sortedX=sorted(random_values)
start_time=time()
linear_search(random_values,999999)
end_time=time()
time_taken=end_time-start_time
print("Time taken for the operation is ",time_taken)
