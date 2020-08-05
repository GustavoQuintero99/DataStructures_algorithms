class test_case(object):
    def __init__(self,matrix,number,expected_answer):
        self.matrix = matrix
        self.number = number
        self.expected = expected_answer
    def call_test(self):
        if rotate_image(self.matrix) == self.expected:
            print("Test case #"+str(self.number)+" result: passed")
        else:
            print("Test case #" + str(self.number) + " result: failed")


def rotate_image(image):
    len_image = len(image)
    if len_image == 0 or len(image[0]) != len_image:
        return image
    for layer in range(len_image):
        for index in range(layer,len_image):
            image[layer][index],image[index][layer] = image[index][layer],image[layer][index]
    for layer in range(len_image):
        L = 0
        R = len_image-1
        while L <= R:
            image[layer][L],image[layer][R] = image[layer][R],image[layer][L]
            L += 1
            R += -1
    return image

if __name__ == '__main__':
    case1 = test_case([[7,4,3],[6,9,4],[1,3,2]],1,[[1,6,7],[3,9,4],[2,4,3]])
    case1.call_test()