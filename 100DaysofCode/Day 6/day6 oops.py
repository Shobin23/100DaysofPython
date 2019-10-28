import random
from collections import namedtuple, defaultdict, Counter, deque

# sort of alternative to dict
User = namedtuple('user','name role')
user = User(name='bob',role='coder')
print('{} is a {}'.format(user.name,user.role))

# use default dict to build up a nested data structure. You dont get keyerror
challenges = defaultdict(list)
for user in users:
    ch = random.sample(challenge_numbers,3)
    challenges[user.role].append(ch)

# counter counts occcurance of words in a list
Counter(list).most_common(5)

#deque , list at push pop at both ends of the sequence/
lst = list(range(100000))
deq = deque(range(100000))