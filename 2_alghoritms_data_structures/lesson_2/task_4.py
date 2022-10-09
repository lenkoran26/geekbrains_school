def sum_seq(count, start=1, sum=1):
    if count == 1:
        return sum
    else:
        start *= -0.5
        sum += start
        count -= 1
    return sum_seq(count, start, sum)

count = 3

print(sum_seq(count))
