
def smallest_dif(arr1,arr2):
	arr1.sort() # Sorting array takes O(logN) time complexity so i wont affect our final time 
	arr2.sort()
	L = 0
	R = 0
	current_pair = [arr1[0],arr2[0]]
	while L < len(arr1) and R < len(arr2):
		first_num = arr1[L]
		second_num = arr2[R]
		if first_num < second_num:
			if abs(first_num-second_num) < abs(current_pair[0]-current_pair[1]):
				current_pair[0],current_pair[1] = first_num,second_num
			L += 1
		elif first_num > second_num:
			if abs(first_num-second_num) < abs(current_pair[0]-current_pair[1]):
				current_pair[0],current_pair[1] = first_num,second_num
			R += 1
		else:
			return [first_num,second_num]
	return current_pair


if __name__ == '__main__':
	x = list(map(int,input().split()))
	y = list(map(int,input().split()))
	print(smallest_dif(x,y))