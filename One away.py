class test_case(object):
    def __init__(self,string1,string2,number,expected_answer):
        self.string1 = string1
        self.string2 = string2
        self.number = number
        self.expected = expected_answer
    def call_test(self):
        if one_away(self.string1,self.string2) == self.expected:
            print("Test case #"+str(self.number)+" result: passed")
        else:
            print("Test case #" + str(self.number) + " result: failed")

# Time complexity : O(N) | Space complexity O(1)
def one_away(s1,s2):
    if len(s1) == 1 and len(s2) == 1:
        return True
    if abs(len(s1)-len(s2)) >= 2:
        return False
    possible_chanes = 0
    current_index = 0
    while possible_chanes <= 1:
        if current_index == max(len(s1),len(s2)):
            break
        try:
            if s1[current_index] == s2[current_index]:
                current_index += 1
            elif s1[current_index] != s2[current_index]:
                current_index += 1
                possible_chanes += 1
        except:
            if abs(len(s1)-len(s2)) == 1:
                if current_index == min(len(s1),len(s2)):
                    return True
    if possible_chanes > 1:
        return False
    else:
        return True

if __name__ == '__main__':
    case1 = test_case("Test","Tes",1,True)
    case2 = test_case("TCB","T",2,False)
    case3 = test_case("T","C",3,True)
    case4 = test_case("Polo","Bolo",4,True)
    case1.call_test()
    case2.call_test()
    case3.call_test()
    case4.call_test()