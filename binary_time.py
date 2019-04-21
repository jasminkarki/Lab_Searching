from time import time
import random
#from binary_search import binary_search
from linear_search import linear_search
import matplotlib.pyplot as plt

#For calculating the time required to search 999999. Uncomment this
'''
random_values =random.sample(range(1000000),1000000)
sortedX=sorted(random_values)
start_time=time()
binary_search(random_values,999999)
end_time=time()
time_taken=end_time-start_time
print("Time taken for the operation is ",time_taken)

'''
class plotComplexity:
	def plotComplexityLinear(self):
		random_values =random.sample(range(1000000),1000000)
		sortedX=sorted(random_values)
		time_taken={}
		step_size=10000

		for _ in range(int(len(sortedX)/step_size)):
			start_time=time()

			x=linear_search(sortedX,sortedX[-1])
			#x=binary_search(sortedX,sortedX[-1])
			
			end_time=time()
			time_taken[len(sortedX)]=end_time-start_time
			sortedX=sortedX[step_size:]	
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
