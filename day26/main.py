# def title_case(title, minor_words=''):
#     if not minor_words:
#         return title.title()
    
#     words = title.split()
#     temp = minor_words.split()

#     res = [words[0].title()]

#     for w in words[1:]:
#         d = w.title()

#         for t in temp:
#             if w.lower() == t.lower():
#                 d = t.lower()

#         res.append(d)
#     return ' '.join(res)

# print(title_case('THE WIND IN THE WILLOWS', 'The In'))

# def title_case(title, minor_words=''):
#     title = title.capitalize()
#     title = title.split()
#     lst = []
#     minor_words = minor_words.lower()
#     minor_words = minor_words.split()
#     for word in title:
#         if word in minor_words:
#             lst.append(word)
#         else:
#             lst.append(word.capitalize())
#     return " ".join(lst)

# print(title_case('THE WIND IN THE WILLOWS', 'The In'))

def diamond(n):
    if n > 0 and n % 2 != 0:
        result = '*' * n + '\n'
        n -= 2
        spaces = 1

        while n > 0:
            current = ' ' * spaces + '*' * n + '\n'
            result = current + result + current
            n -= 2
            spaces += 1

        return result
    
print(diamond(11))