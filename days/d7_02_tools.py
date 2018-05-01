list_info = []
list_field = ["Index", "name", "phone", "qq", "mail"]


def show_menu():
    print(
        """%s
Welcome to card system V1.0

1.create card
2.show all
3.search card

0.out
%s""" % ("*" * 30, "*" * 30))


def print_all(list_):
    # check the max length of element
    len_max = [5] * 4
    for dicts_user in list_:
        for i in range(4):
            len_max[i] = max(len_max[i], len(dicts_user[list_field[i+1]]))
    # print head
    print("Index", end=" ")
    for i in range(4):
        print(list_field[i+1].ljust(len_max[i]), end=" ")
    print()
    # print body
    print("%s" % ("-" * (sum(len_max) + 9)))
    index_num = 0
    for dicts_user in list_:
        index_num += 1
        print("%-5d" % index_num, end=" ")
        for i in range(4):
            print(dicts_user[list_field[i+1]].ljust(len_max[i]), end=" ")
        print()
    print("%s\n" % ("-" * (sum(len_max) + 9)))


def create_card():
    print("function: create_card")
    name = input("pls enter name: ")
    phone = input("pls enter phone: ")
    qq = input("pls enter qq: ")
    mail = input("pls enter mail: ")
    # save data
    dict_user = {"name": name, "phone": phone, "qq": qq, "mail": mail}
    list_info.append(dict_user)
    print("Card has been created.\n")


def show_all():
    print("function: show all\n")
    if len(list_info) == 0:
        print("NO RECORD!\n")
        return  # 由于不是在循环里，故不用 break
    list_temp = list_info
    print_all(list_temp)


def search_card():
    print("function: card searching\n")
    while True:
        if len(list_info) == 0:
            print("NO RECORD!\n")
            break
        search_field = input("""pls enter searching Field:
    1.name(or press enter) 2.phone 3.qq 4.mail / 0.Exit : """)
        if search_field not in ["1", "2", "3", "4", "0", ""]:
            print("WRONG INPUT!\n")
        elif search_field == "0":
            break
        else:  # print search result
            if search_field == "":
                search_field = "1"
            search_field = int(search_field)
            search_keyword = input("pls enter %s: " % list_field[search_field])
            # searching
            list_temp = []
            i = 0
            for dicts_user in list_info:
                if search_keyword == dicts_user[list_field[search_field]]:
                    list_temp.append(dicts_user)
                    i += 1
            if i == 0:
                print("NO result!\n")
                break
            print_all(list_temp)
            operate_num = input("pls enter operate:\n\t1.Edit 2.Del / 0.Exit")
            if operate_num == "1":
                card_edit(list_temp, i)
                break
            elif operate_num == "2":
                card_del(list_temp, i)
                break
            elif operate_num == "0":
                break
            else:
                print("WRONG INPUT!\n")


def card_edit(list_, index_sum):
    # 选择要修改列的序号，判断输入是否规范
    index_num = input_judgement(index_sum)
    # 修改具体值
    name = input("pls enter name(press Enter to skip): ")
    phone = input("pls enter phone(press Enter to skip): ")
    qq = input("pls enter qq(press Enter to skip): ")
    mail = input("pls enter mail(press Enter to skip): ")
    change_flag = 0
    for k, v in zip(list_field[1:], [name, phone, qq, mail]):
        if not v == "":
            list_[index_num][k] = v
            change_flag += 1
    # 提示修改结果
    if change_flag == 0:
        print("Nothing changed.\n")
    else:
        print("Card %d has been changed.\n" % (index_num + 1))


def card_del(list_, index_sum):
    # 选择要删除列的序号，判断输入是否规范
    index_num = input_judgement(index_sum)
    # 从总 list 中删除列
    list_info.remove(list_[index_num])
    print("Card has been deleted.\n")


def input_judgement(index_sum):
    index_num = 0
    if index_sum > 1:
        while True:
            # index_num = input("pls enter index: ")
            # if not index_num.isdecimal():
            #     print("WRONG INPUT!\n")
            #     continue
            # index_num = int(index_num) - 1
            try:
                index_num = input("pls enter index: ")
                index_num = int(index_num) - 1
            except BaseException:
                print("pls enter num")
            break
    return index_num
