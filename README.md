# transleet
translate normal text to leet(l33t)

## Examples:
```python
print(transleet('the quick brown fox jumps over the lazy dog'))
# >>> '7#3 qu1(% 6r0wn f08 jump5 0v3r 7#3 |42y d09'
print(transleet('7#3 qu1(% 6r0wn f08 jump5 0v3r 7#3 |42y d09'))
# >>> 'the quick brown fox jumps over the lazy dog'

print(transleet('the quick brown fox jumps over the lazy dog', unicode=True))
# >>> '7#3 qµ1(κ 6γ0ωn ≠08 jµmρ5 0ν3γ 7#3 |42y δ09'
print(transleet('7#3 qµ1(κ 6γ0ωn ≠08 jµmρ5 0ν3γ 7#3 |42y δ09', unicode=True))
# >>> 'the quick brown fox jumps over the lazy dog'
```
