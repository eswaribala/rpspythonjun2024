from collections import Counter
#counter
list1 = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list1)
print(cnt[2]) #counts no of 2's

#elements
cnt = Counter({1:3,2:4})
print(list(cnt.elements()))

#most_common()

list1 = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list1)
print(cnt.most_common())

#subtract
cnt = Counter({1:3,2:4}) #key:value
deduct = {1:1, 2:2} #key:value
cnt.subtract(deduct) #{1:2,2:2}
print(cnt)

def test():
    return 5


from collections import defaultdict
nums = defaultdict(type('a'))
nums['one'] = 1
nums['two'] = 2
print('default....')
print(nums['three'])



from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)



from collections import deque
list = ["a","b","c"]
deq = deque(list)
deq.popleft()
print(deq)
deq.pop()
print(deq)



from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'b': 4}
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)
for _  in chain_map.maps:
    print (_.keys())



from collections import namedtuple

Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '13')
print(s1.fname)

