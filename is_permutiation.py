#Given an string S and string C verify if one string is permutation of the other
class test_case(object):
    def __init__(self,val,val2,number,expected):
        self.number = number
        self.val = val
        self.val2 = val2
        self.expected_answer = expected
    def call_test_case(self):
        if is_permutiation(self.val,self.val2) == self.expected_answer:
            print("Test case #"+str(self.number)+" status : Passed")
        else:
            print("Test case #"+str(self.number)+" status : Failed")

# Timec complexity O(N) | Space complexity O(1)
def is_permutiation(S,C):
    if len(S) != len(C):
        return False
    for each in S:
        if C.count(each) != S.count(each):
            return False
    return True

# Time complexity O(log n)| Space complexity O(n)
'''
def is_permutiation(S,C):
    list1,list2 = list(S),list(C)
    list1.sort()
    list2.sort()
    return list1 == list2
'''

if __name__ == '__main__':
    caso1 = test_case("ABC","BCA",1,True)
    caso2 = test_case("tago","gato",2,True)
    caso3 = test_case("tato","tatu",3,False)
    caso4 = test_case("papapapapapale","lepapapapapapa",4,True)
    caso5 = test_case("pablo","oblapp",5,False)
    caso1.call_test_case()
    caso2.call_test_case()
    caso3.call_test_case()
    caso4.call_test_case()
    caso5.call_test_case()