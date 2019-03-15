class AutoVideo():
    @staticmethod
    def videoNum():
        file = open("/home/nvidia/5549/PycharmProjects/OpenCV/5549-vision/num", "r")
        number = file.readline()
        new_num = int(number) + 1
        print("Next Video # is: " + str(new_num))
        file = open("num", "w+")
        file.write(str(new_num))