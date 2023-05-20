'Mn cho em hỏi làm thế nào để tách số nguyên ra khỏi chuỗi.Em muốn tách "5ab-65dh-6 5"  thành [5,-65,-6,5] phải làm kiểu j ạ,mong mn giúp đỡ cho em '
# import re

# numbers = re.compile('-?\d+')
# ts = "5ab-65dh-6 5"
# result = list(map(int, numbers.findall(ts)))
# print(result)


# def century_from_year(year):
#     return (year + 99) // 100


# print(century_from_year(2020) == 21)
# print(century_from_year(200) == 2)
# print(century_from_year(2005) == 21)
# print(century_from_year(1700) == 17)
# print(century_from_year(1705) == 1 8)

def rain_amount(mm):
    if mm >= 40:
        return "Your plant has had more than enough water for today!"
    else:
        return f"You need to give your plant {40 - mm}mm of water"
