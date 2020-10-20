

def repr_is_equal(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    i1 = 0
    i2 = 0

    while True:
        if s1[i1] != s2[i2]:
            return False

        if i1 == n1-1 and i2 == n2-1:
            return True # we finished both strings and found no mismatch

        # advance i1 index until the next different character or end of string
        for i1 in range(i1+1, n1):
            if s1[i1] != s1[i1-1]:
                break

        # advance i2 index until the next different character or end of string
        for i2 in range(i2+1, n2):
            if s2[i2] != s2[i2-1]:
                break


###############################################################################
assert repr_is_equal('a', 'a') == True
assert repr_is_equal('aa', 'a') == True
assert repr_is_equal('a', 'aa') == True
assert repr_is_equal('a', 'ab') == False
assert repr_is_equal('ab', 'a') == False
assert repr_is_equal('ab', 'ba') == False
assert repr_is_equal('a', 'aaaba') == False
assert repr_is_equal('aaaaaaabbbbbbccccccdddddd', 'aaaabbbbcccd') == True
assert repr_is_equal('aaaabbbbbcccccddde', 'abcd') == False
assert repr_is_equal('aaaaaaabbbbbbccccccdddddd', 'abcddde') == False
assert repr_is_equal('abcdef', 'abcddddddddeffffff') == True

print('All good!')
