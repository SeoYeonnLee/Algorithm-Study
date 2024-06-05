word = input()
word= word.upper()
word_dict = {}

for s in word:
    if s not in word_dict:
        word_dict[s] = 1
    else:
        word_dict[s] += 1

max_cnt = max(word_dict.values())

if list(word_dict.values()).count(max_cnt) > 1:
    print('?')
else:
    for w, cnt in word_dict.items():
        if cnt == max_cnt:
            print(w)