def letterCombinations(digits):
    dict = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', 
    '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz' }
    cmb = [''] if digits else []
    for d in digits:
        cmb = [a + b for a in cmb for b in dict[d]]
    return cmb

print(letterCombinations(['2','3','4']))