def calculate(item_list):
    item_1 = (item_list[0] * 8.9)
    item_2 = (item_list[1] * 7.5)
    item_3 = (item_list[2] * 0.85)
    item_4 = (item_list[3] * 0.55)
    item_5 = (item_list[4] * 0.65)
    item_6 = (item_list[5] * 0.65)
    item_7 = (item_list[6] * 0.65)
    item_8 = (item_list[7] * 2.4)

    total = item_1 + item_2 + item_3 + item_4 + item_5 + item_6 + item_7 + item_8

    return item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, total

