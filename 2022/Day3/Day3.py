
import datetime


PRIOR = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

f = open("Day3/Inputdata.txt", "r")

def p1(f):
  ans = 0
  for line in f.read().split():
    m = len(line) //2
    a = line[:m]
    b= line[m:]
    c= set(a) & set(b)
    ans += PRIOR.index(next(iter(c)))
  return ans

def p2(f):
  ans = 0
  lines = iter(f.read().split())
  while True:
    try:
      a,b,c = next(lines),next(lines), next(lines)
    except StopIteration:
      return ans

    d= set(a) & set(b) & set(c)
    ans += PRIOR.index(next(iter(d)))


starttime = datetime.datetime.now()
print(p2(f))
endtime = datetime.datetime.now() - starttime
print((endtime.total_seconds() * 1000))