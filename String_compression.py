class test_case(object):
    def __init__(self,string1,number,expected_answer):
        self.string1 = string1
        self.number = number
        self.expected = expected_answer
    def call_test(self):
        if string_compression(self.string1) == self.expected:
            print("Test case #"+str(self.number)+" result: passed")
        else:
            print("Test case #" + str(self.number) + " result: failed")

# Iterate over the array and count which characters appers
# Count how many characters of each does apper in my array
# Append the count of each character and return it as string


# Time complexity O(N) | Space complexity O(N) or O(1) since its only going to hold up to 256 char
def string_compression(given_string):
    new_hash = {}
    former_string = given_string
    given_string = sorted(given_string)
    final_array = ""
    for each in given_string:
        try:
            new_hash[each] += 1
        except:
            new_hash[each] = 1
    for each in new_hash.keys():
        final_array += str(each)
        final_array += str(new_hash[each])
    if len(former_string) <= len(final_array):
        return former_string
    return final_array

if __name__ == '__main__':
    case1 = test_case("aabccccaa",1,"a4b1c4")
    case2 = test_case("abcd",2,"abcd")
    case3 = test_case("aabbccdd",3,"aabbccdd")
    case4 = test_case("oooooooooooofffffffffffaaaaaaassssssssso",4,"a7f11o13s9")
    case1.call_test()
    case2.call_test()
    case3.call_test()
    case4.call_test()