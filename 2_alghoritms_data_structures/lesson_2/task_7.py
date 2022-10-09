def arif_prog(n, i=1, sum=0, txt=''):
    if i > n:
        txt = txt[:len(txt)-1] # txt.rstrip('+') не сработал в функции, хотя при тестировании работало '1+2+3+'.rstrip('+')=='1+2+3'
        txt += ' ='
        return sum, txt
    else:
        sum += i
        txt += f'{i}+'
        i += 1
        return arif_prog(n, i, sum, txt)

n = 5
sum_arifm_prog_recur, txt = arif_prog(n)
sum_arifm_prog = n*(n+1)/2

if sum_arifm_prog_recur == sum_arifm_prog:
    print('Equality is True')
    print(f'{txt} {n}*({n}+1)/2')