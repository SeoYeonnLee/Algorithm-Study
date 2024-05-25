import sys

N = int(sys.stdin.readline())
score_list = list(map(int, sys.stdin.readline().split()))
max_score = max(score_list)

new_score_list = [(score/max_score)*100 for score in score_list]
print(sum(new_score_list)/N)