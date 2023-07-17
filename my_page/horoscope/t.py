def filter_string(text, char):
    a = text
    for i in text:
        if i.lower() == char.lower():
            a = a.replace(i, '')
    print(a)


text = 'If I look forward I win'
filter_string(text, 'i')  # 'f  look forward  wn'
filter_string(text, 'O')  # 'If I lk frward I win'