import time
import random
import matplotlib.pyplot as plt
from binary_search import binary_search
from linear_search import linear_search



class plotComplexity:
	def plotComplexityLinear(self):
		random_numbers = random.sample(range(1000000),1000000)
		sorted_number = sorted(random_numbers)
		time_taken = {}
		step_size = 10000

		for _ in range(int(len(sorted_number)/step_size)):
			start_time = time.clock()
			#x = linear_search(sorted_number, sorted_number[-1])
			x = binary_search(sorted_number, sorted_number[-1])
			end_time = time.clock()
			time_taken[len(sorted_number)] = end_time - start_time
			sorted_number = sorted_number[step_size:]
		return time_taken

plotLinearSearch = plotComplexity()

timetakenDict = plotLinearSearch.plotComplexityLinear()

dataNumbers = []
times = []

for key in sorted(timetakenDict):
	dataNumbers.append(key)
	times.append(timetakenDict[key])

plt.plot(dataNumbers, times)
plt.xticks(dataNumbers)
plt.yticks(times)
plt.show()
