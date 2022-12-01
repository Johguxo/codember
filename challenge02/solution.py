import re
def ascii_to_text(number):
    list_char = []
    ascii_item = ''
    for item in number:
        ascii_item += item
        if int(ascii_item) >= 97 and int(ascii_item) <= 122:
            list_char.append(chr(int(ascii_item)))
            ascii_item = ''
    return ''.join(list_char)

#text = '99111100101109981011140 109105100117 112108971210 116101116114105115'
text = '11610497110107115 102111114 11210897121105110103 9911110010110998101114 11210810197115101 11510497114101'
list_items = text.split(' ')

result = []
for item in list_items:
  result.append(ascii_to_text(item))

print(' '.join(result))