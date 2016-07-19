# Ignore the first number
for i in range(int(raw_input())):
	# Get the input
	s = raw_input();
	# s[::2] = split the even indexes
	print(s[::2]+" "+s[1::2])
