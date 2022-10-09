def ascii_decode(position=32, txt='', colum=1):
    if position > 127:
        return txt
    else:
        txt += str(position) + ' - ' + chr(position) + ' '
        colum += 1
        if colum > 10:
            txt += '\n'
            colum = 1
    return ascii_decode(position + 1, txt, colum)

print(ascii_decode())