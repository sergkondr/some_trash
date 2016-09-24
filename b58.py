abc = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnopqrstuvwxyz'

def to_b58(div):
    ret = ''
    while div != 0:
        div, mod = divmod(div, len(abc))
        ret += abc[mod]
    return ret[::-1]

def from_b58(num):
    div = 0
    for mod in num:
        div = div * len(abc) + abc.find(mod)
    return div