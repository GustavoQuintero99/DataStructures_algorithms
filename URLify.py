#Given an string "string" replace all the spaces after the first one with %20
class test_case(object):
    def __init__(self,val,number,expected):
        self.number = number
        self.val = val
        self.expected_answer = expected
    def call_test_case(self):
        if URLify(self.val) == self.expected_answer:
            print("Test case #"+str(self.number)+" status : Passed")
        else:
            print("Test case #"+str(self.number)+" status : Failed")

# Time complexity O(N) | Space complexity O(N)
def URLify(string):
    new_list = list(string)
    first_letter = False
    for each in reversed(range(len(new_list))):
        if new_list[each] == " " and first_letter == False:
            new_list.pop(each)
        elif new_list[each].isalnum() == True:
            first_letter = True
            continue
        elif new_list[each] == " " and first_letter == True:
            new_list[each] = "%20"
    return "".join(new_list)

if __name__ == '__main__':
    caso1 = test_case("Gustavo Quintero",1,"Gustavo%20Quintero")
    caso2 = test_case("Mr Software Engineer  ",2,"Mr%20Software%20Engineer")
    caso3 = test_case("I want to get in google",3,"I%20want%20to%20get%20in%20google")
    caso4 = test_case("Ya no se que poner ",4,"Ya%20no%20se%20que%20poner")
    caso1.call_test_case()
    caso2.call_test_case()
    caso3.call_test_case()
    caso4.call_test_case()