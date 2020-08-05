class test_case(object):
    def __init__(self,matrix,number,expected_answer):
        self.matrix = matrix
        self.number = number
        self.expected = expected_answer
    def call_test(self):
        if set_zero(self.matrix) == self.expected:
            print("Test case #"+str(self.number)+" result: passed")
        else:
            print("Test case #" + str(self.number) + " result: failed")


def set_zero(matrix):
    zereos_founded = {}
    current_key = 1
    for layer in range(len(matrix)):
        for index in range(len(matrix[layer])):
            if matrix[layer][index] == 0:
                zereos_founded[current_key] = index,layer
                current_key += 1
    for each in zereos_founded.values():
        zero_found(matrix,each[0],each[1])
    print(matrix)
    return matrix

def zero_found(matrix,index,layer):
        for layer2 in range(len(matrix)):
            if layer != layer2:
                matrix[layer2][index] = 0
        for index3 in range(len(matrix[layer])):
            matrix[layer][index3] = 0
        return matrix


if __name__ == '__main__':
    case1 = test_case([[7,4,3],[6,9,4],[1,0,2]],1,[[7,0,3],[6,0,4],[0,0,0]])
    case2 = test_case([[2,1,1],[4,0,6],[2,3,9]],2,[[2,0,1],[0,0,0],[2,0,9]])
    case3 = test_case([[0,1,2,0],[3,4,5,2],[1,3,1,5]],3,[[0,0,0,0],[0,4,5,0],[0,3,1,0]])
    case1.call_test()
    case2.call_test()
    case3.call_test()