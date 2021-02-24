# for i in range(6):
#     print(i)


# range(5, 10)

# a = ['konya', 'Sakura', 'no', 'ki', 'no', 'shita', 'de']
# for i in range (len(a)):
#         print(i, a[i])


## enumerate ##

# enumerate(iterable, start=0)
  
# Return enumerate object 
#        -> __next__() return tuple containing a count  
#

# iterable <- iterator or other object support iteration


seasons = ['spring', 'summer', 'fall', 'winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))


def enumerate1(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

for x in enumerate1(seasons):
    print(x)

print(list(range(10)))
