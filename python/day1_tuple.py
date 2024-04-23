"""
Tuple:
Tuple : fixed length, immutable(once assigned, can't be changed)
"""


class MainClass:
    def main_method(self):
        tup = (4, 5, 6)
        print(tup)
        print((type(tup)))

        tup1 = tuple([4, 5, 6])
        print(tup1)
        print(type(tup1))

        tup3 = tuple(['foo', [1, 2], True])
        # tup3[2] = False

        # Objects stored inside the tuple coule be mutable themselves, but tuple is always immutable.
        tup3[1].append(4)
        print(tup3)

        # Concatenation:
        tup_concat = (4, None, 'foo') + (6, 0) + ('bar',)
        print(tup_concat)

        # Tuple Methods:
        a = (1, 2, 2, 2, 3, 4, 2)
        print(a.count(2))


if __name__=='__main__':
    MainClass().main_method()