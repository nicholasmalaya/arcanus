def read_data(filename):
# Read filename where filename starts with comment lines
# defined by symbol '#' then contains data in 2 columns
# of identical length
	inp = open(filename, 'r')
	myline = inp.readline()
	while myline[0] == '#':
		myline = inp.readline()

	t = []; h = []
	while myline:
		mls = myline.split()
		t.append(float(mls[0]))
		h.append(float(mls[1]))
		myline = inp.readline()
		
	inp.close()

	return t, h
