def answer(string, k):
    string_list = list(string)
    string_list.insert(int(k), "=")
    string_list = "".join(string_list)
    string_list = string_list.split("=")
    string_list[0], string_list[1] = string_list[1], string_list[0]
    return("".join(string))

if __name__ == "__main__":
    print("enter an string that will rotate arount the k")
    inp1 = input(">> ")
    print("enter the k \nthe k start from 0th")
    inp2 = input(">> ")
    print("answer : " + answer(inp1, str(inp2)))


"""
first split the string by k th posion

"""