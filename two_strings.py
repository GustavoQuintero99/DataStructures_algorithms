def solution(s1,s2):
	for each in s1:
		if each in s2:
			print("YES")
			return
	print("NO")

if __name__ == '__main__':
	test_cases = int(input())
	for each_case in range(test_cases):
		string1 = input()
		string2 = input()
		solution(string1,string2)




'''
2
hello
world
hi
world

'''