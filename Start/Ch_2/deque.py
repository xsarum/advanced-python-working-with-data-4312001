# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
print(f"item count: {len(d)}")

# TODO: deques can be iterated over
for ele in d:
    print(ele.upper())

# TODO: manipulate items from either end
d.pop() # removes a
d.popleft() # removes z
d.append(2) # adds 2 to end 
d.appendleft(1) # adds 1 to beginning
print(d)

# TODO: use an index to get a particular item
print(d)
d.rotate(1) # rotates one space to the right 
print(d)