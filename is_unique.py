#Given an string S verify if it has all unique characters
class test_case(object):
    def __init__(self,val,number,expected):
        self.number = number
        self.val = val
        self.expected_answer = expected
    def call_test_case(self):
        if is_unique(self.val) == self.expected_answer:
            print("Test case #"+str(self.number)+" status : Passed")
        else:
            print("Test case #"+str(self.number)+" status : Failed")

# Cracking the coding interview solution
# Time complexity O(1) | Space complexity O(1)
def is_unique(S):
    # If the len of the string its bigger than 128 characters that means we exceed the ascii values
    if len(S) > 128:
        return False
    char_set = [None]*128
    # Creating the array with all possible ascii values initialized as None
    for index in range(len(S)):
        # If a index with the ascii value already exist in my array, that means it appears twice or more
        if char_set[ord(S[index])]:
            return False
        else:
            # If its the first time we see that specific value just add it to the array
            char_set[ord(S[index])] = True
    return True

'''
# Time complexity : O(N) | Space complexity O(N)    
def is_unique(S):
    each_char = {}
    S = S.lower()
    for each in S:
        if each in each_char.keys():
            return False
        each_char[each] = True
    return True
'''

# Time complexity : O(N°2) | Space complexity O(1)
'''
def is_unique(S):
    S = S.lower()
    for first in range(len(S)):
        for second in range(len(S)):
            print(S[first],S[second])
            if first != second and S[first] == S[second]:
                return False
    return True
'''


if __name__ == '__main__':
    caso1 = test_case("abcdefg",1,True)
    caso2 = test_case("pinguino",2,False)
    caso3 = test_case("abderta",3,False)
    caso4 = test_case("cestrE",4,True)
    caso5 = test_case("mustbe",5,True)
    caso1.call_test_case()
    caso2.call_test_case()
    caso3.call_test_case()
    caso4.call_test_case()
    caso5.call_test_case()