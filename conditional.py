import sys

inputInt = int(sys.stdin.readline())

if inputInt % 2 == 1 :
	print("Weird")

elif inputInt <= 5 :
	print("Not Weird")

elif inputInt <= 20 :
	print("Weird")

else :
	print("Not Weird")