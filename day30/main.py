""" def domain_name(url):
    url = url.replace("http://", '')
    url = url.replace("www.", '')
    url = url.replace("https://", '')
    index_period = url.find('.')
    return url[0:index_period]

print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))

def first_non_consecutive(arr):
    ans = None
    for x in range(len(arr) - 1):
        if arr[x] + 1 != arr[x + 1]:
            ans = arr[x + 1]
    return ans

print(first_non_consecutive([1,2,3,4,6,7,8]) == 6)


def solution(s):
    lst = []
    for x in s:
        if x.isupper():
            lst.append(' ' + x)
        else:
            lst.append(x)
    return ''.join(lst)


print(solution("helloWorld") == "hello World")
print(solution("camelCase") == "camel Case")
print(solution("breakCamelCase") == "break Camel Case") """

""" la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5
total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals
print(f'total goals should equal to {total_goals}') """
from numpy import prod
a = [3,4,5]
b = [6,5,7]

print(abs(prod(a)-prod(b)))