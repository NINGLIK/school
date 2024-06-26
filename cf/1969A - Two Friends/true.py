for _ in range(int(input())):
	number=int(input())
	bestfriend=list(map(int,input().split()))
	minloop=3
	# 寻找两个成对是好友的朋友
	for _ in bestfriend:
		if bestfriend.index(_)+1==bestfriend[_-1]:
			minloop=2
			break
	print(minloop)