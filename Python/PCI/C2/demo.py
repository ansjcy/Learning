from recommendation import critics
import recommendation
import pydelicious
from deliciousrec import *
a = recommendation.sim_distance(recommendation.critics,
                                    'Lisa Rose',
                                    'Gene Seymour')
print(a)
a = recommendation.topMatches(recommendation.critics,
                                      'Toby', n = 3)
print(a)

#test function setdefault..
b = {}
b.setdefault('ha', 2)
b['xi'] = 3
for i in b:
    print(i)
    b['ha'] += 1
    b.setdefault('ha', 2)
print(b['ha'])

#test for in in dictionary..
set = {'a':0,'b':1,'c':2}
res = [(val/0.5,key) for key,val in set.items()]
res.sort()
print(res)



