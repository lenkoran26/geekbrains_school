import hashlib
def substring(substr: str):
    set_of_substring = set()
    for i in range(0, len(substr)+1):
        for j in range(i+1, len(substr)+1):
            if substr != substr[i:j]:
                sub = substr[i:j]
                hash_substr = hashlib.md5(sub.encode('utf-8')).hexdigest()
                set_of_substring.add(hash_substr)
    return set_of_substring

txt = 'papa'
permut = substring(txt)
print(f'В строке "{txt}"')
print(f'Количество перестановок = {len(permut)}')
print(permut)
