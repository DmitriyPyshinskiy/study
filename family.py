import sys

def func(x):
    l = []
    for i in range(x + 1):
	if i%2 == 0 and i<=x:
	    l.append(i)
    return l

print(func(int(sys.argv[1])))
