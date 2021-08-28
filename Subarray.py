
def hasZeroSumSublist(A):
	s = set()
	s.add(0)

	sum = 0
	for i in A:
		sum += i
		if sum in s:
			return True
		s.add(sum)
	return False


n=int(input())
A = [int(x) for x in input().split(",")]
if hasZeroSumSublist(A):
    print("1")
else:
	print("0")
