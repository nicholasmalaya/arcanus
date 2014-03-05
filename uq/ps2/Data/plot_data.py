import os
import matplotlib.pyplot as plt
from matplotlib import rc

import read_data as rd

def plot_data(extension):
# Plot data file with a given extension
	rc('text', usetex=False)

	fig = plt.figure()
	ax = fig.add_subplot(111)

	label = []
	for file in os.listdir('.'):
		if file.endswith(extension):
			t, h = rd.read_data(file)
			ax.plot(t, h, 'o-', label=file)

	ax.legend()
	plt.show(block=True)


if __name__ == '__main__':
	plot_data('dat')
