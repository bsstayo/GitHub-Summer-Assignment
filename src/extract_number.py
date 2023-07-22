def extract_number(results):
    tmp = []

    for n in range(1, 7):
        tmp_string = 'drwtNo' + str(n)
        tmp.append(results.get(tmp_string, None))
    tmp.append(results.get('bnusNo', None))

    return tmp
