## Find the longest subpalindrome in the string
## The cases of letters does not matter, but whitespace is not allowed 
## in the subpalindromes.

## return index tuple (i, j) where
## i is the start of the palindrome
## and j is 1 behind the end
## Algorithm Complexity is O(n**2), and the best is O(n)
def longest_palindrome_slice(text):
    def extend(i, j):
        while (i >= 0 and j < len(text)
            and text[i].upper() == text[j].upper()):
            i -= 1
            j += 1
        return (i+1, j)
    candidates = [
        extend(i-1, j)
        for i in range(len(text))
        for j in (i, i+1)
    ]
    return max(candidates, key = lambda (start, end): end-start)

## tests
if __name__ == '__main__':
    ## test longest_palindrome_slice
    (i, j) = longest_palindrome_slice("Racecar")
    assert 'Racecar'[i:j] == 'Racecar'
    (i, j) = longest_palindrome_slice('I got my eyes on you.')
    assert 'I got my eyes on you.'[i:j] == 'eye'
    (i, j) = longest_palindrome_slice('Murder for a jar of red rum.')
    assert 'Murder for a jar of red rum.'[i:j] == ' a ' # whitespace does count in palindrome
    
    print 'all tests pass'