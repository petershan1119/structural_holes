from jnet import one_mode_network
from jnet import two_mode_network
from jnet import create_random_tm_net
import matplotlib
import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import operator
import collections
from scipy import stats
import sys
import math

def get_data(filename):
	xl = pd.ExcelFile(filename)
	df = xl.parse("Page 1")
	df = df.as_matrix()
	data = df.tolist()

	for row in data:
		del row[0]
	return data


data = get_data("FILE_NAME.txt")


tm_net = two_mode_network(data)

# assign weights from both perspectives (i.e. both sets as primary)
# keep track in separate adj matrices
tm_net.assign_weights(True)
#tm_net.assign_weights(False)


om_net_data = tm_net.project(True, True)


#om_net_data = tm_net.project(False, True)

om_net = one_mode_network(om_net_data)


x = collections.OrderedDict()
y = collections.OrderedDict()

om_degree = []
tm_degree = []

for i in range(len(om_net.adj)):

	x[i] = tm_net.get_effective_size(i, True)
	#x[i] = tm_net.get_effective_size(i, False)
	y[i] = om_net.get_effective_size(i)
	om_degree.append(len(om_net.get_contacts(i)))
	tm_degree.append(len(tm_net.get_contacts(i, True)))
	#tm_degree.append(len(tm_net.get_contacts(i, False)))


# plot by effective size stuff
x_items = x.items()
x_list = [i[1] for i in x_items]

y_items = y.items()
y_list = [j[1] for j in y_items]


plt.scatter(x_list, y_list, s=1)
plt.xlabel("Two-mode effective size")
plt.ylabel("One-mode effective size")


plt.show()

