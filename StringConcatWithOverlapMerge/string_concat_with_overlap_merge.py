# Concatenate two strings, but merge the overlap between them
# concat('foobar', 'bart') => 'foobart'
# concat('foobarb', 'barbara') => 'foobarbara'
# concat('foobarb', 'bart') => 'foobarbart'

def concat(left, right):
    # Easy cases, handle null
    if not left:
        return right or ''
    if not right:
        return left or ''

    maximum_overlap = min(len(left), len(right))
    start = max(0, len(left)-len(right))
    j = 0
    for i in xrange(start, maximum_overlap+start):
        if left[i:] == right[0:maximum_overlap-j]:
            return left + right[maximum_overlap-j:]
        j += 1

    return left + right

if __name__ == '__main__':
    # Partial overlap
    assert('foobart' == concat('foobar', 'bart'))

    # Partial Overlap
    assert('foobarbara' == concat('foobar', 'barbara'))

    # Partial Overlap
    assert('foobarbara' == concat('foobarb', 'barbara'))

    # Shorter Partial Overlap 
    assert('foobarbart' == concat('foobarb', 'bart'))

    # No overlap
    assert('abcdef' == concat('abc', 'def'))

    # Empty Strings and None edge cases
    assert('bart' == concat('', 'bart'))
    assert('foobar' == concat('foobar', None))
    assert('bart' == concat(None, 'bart'))
    assert('' == concat('', ''))
    assert('' == concat(None, None))
