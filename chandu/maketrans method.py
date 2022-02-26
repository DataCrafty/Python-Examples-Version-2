def s(name):
    l= name.maketrans('s','c')
    s = name.translate(l)
    return s
name='shandu'
s(name)