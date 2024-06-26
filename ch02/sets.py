# sets.py

small_primes = set()  # empty set
small_primes.add(2)  # adding one element at a time
small_primes.add(3)
small_primes.add(5)
print(small_primes)
# {2, 3, 5}

small_primes.add(1)  # Look what I've done, 1 is not a prime!
print(small_primes)
# {1, 2, 3, 5}

small_primes.remove(1)  # so let's remove it
print(3 in small_primes)  # membership test
# True

print(4 in small_primes)
# False

print(4 not in small_primes)  # negated membership test
# True

small_primes.add(3)  # trying to add 3 again
print(small_primes)
# {2, 3, 5}  # no change, duplication is not allowed

bigger_primes = set([5, 7, 11, 13])  # faster creation
print(small_primes | bigger_primes)  # union operator `|`
# {2, 3, 5, 7, 11, 13}

print(small_primes & bigger_primes)  # intersection operator `&`
# {5}

print(small_primes - bigger_primes)  # difference operator `-`
# {2, 3}

small_primes = {2, 3, 5, 5, 3}
print(small_primes)
# {2, 3, 5}

# frozenset
small_primes = frozenset([2, 3, 5, 7])
bigger_primes = frozenset([5, 7, 11])
# small_primes.add(11)  # we cannot add to a frozenset
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'frozenset' object has no attribute 'add'

# small_primes.remove(2)  # neither we can remove
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'frozenset' object has no attribute 'remove'

print(small_primes & bigger_primes)  # intersect, union, etc. allowed
# frozenset({5, 7})
