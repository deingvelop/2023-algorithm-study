s_list = list(input())
just_before = ''
groups = []
cnt = 0

for s in s_list:
    if s != just_before:
        groups.append(s)
    just_before = s

print(min(groups.count('0'), groups.count('1')))