S = input()

zero = S.split('0')
one = S.split('1')

onereverse = len(zero) - (zero.count('')) #1을 뒤집을 때 횟수

zeroreverse = len(one) - (one.count('')) #0을 뒤집을 때 횟수

print(min(onereverse,zeroreverse))
