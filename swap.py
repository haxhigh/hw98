
def swapData():
    file1 = "C:/Users/iliea/OneDrive/Desktop/Python/Hw/HW98/text1.txt"
    file2 = "C:/Users/iliea/OneDrive/Desktop/Python/Hw/HW98/text2.txt"

    with open(file1, "r") as a:
        data_a = a.read()
    with open(file2, "r") as b:
        data_b = b.read()
    with open(file1, "w") as a:
        a.write(data_b)
    with open(file2, "w") as b:
        b.write(data_a)
    for line in data_a:
        print(line)
swapData()
