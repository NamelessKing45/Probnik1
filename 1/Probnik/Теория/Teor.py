i = [56, 9, 11, 2, [3, 81, 5]]
def o():
     c = []
     p = []
     i = [56, 9, 11, 2, [3, 81, 5]]
     for q in i[0:4]:
          p.append(q)
     for w in i[4]:
          p.append(w)
     print(p)
     for q in p:
          c.append(max(p))
          p.remove(max(p))
     print(c)
     return
print(o())
