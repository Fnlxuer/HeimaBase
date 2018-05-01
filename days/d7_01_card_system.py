import d7_02_tools
while True:
    d7_02_tools.show_menu()
    num_str = input("pls enter num:")
    print("your choice:%s" % num_str)
    if num_str == "1":
        d7_02_tools.create_card()
    elif num_str == "2":
        d7_02_tools.show_all()
    elif num_str == "3":
        d7_02_tools.search_card()
    elif num_str == "0":
        print("Good bye.")
        break
    else:
        print("WRONG INPUT! Pls enter right NUM!")
