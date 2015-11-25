def f(v,i,S):
  if i >= len(v): return 1 if S == 0 else 0
  count = f(v, i + 1, S)
  count += f(v, i + 1, S - v[i])
  return count

v = [1, 2, 3, 10]
sum = 12
print(f(v, 0, sum))
