import pandas as pd

result = pd.read_csv("result9.csv")
compare = pd.read_csv("Y_Test_100.csv")

correct = 0

for i in xrange(100):
	if result["Label"][i] == compare["Label"][i]:
		correct += 1
print correct
