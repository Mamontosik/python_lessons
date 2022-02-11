def get_sep(sep, sep_len):
    return sep * sep_len

#возвращаемое значение
sep = get_sep('-', 50)
text = 'Hello {} Func {}'.format(sep, sep)

print(text)
