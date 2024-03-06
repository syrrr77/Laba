syr = 'Воронов'
syr = syr.lower()
slov = {}

for bukvi in syr:
    if bukvi in slov:
        slov[bukvi] += 1

    else:
        slov[bukvi] = 1

print(slov)