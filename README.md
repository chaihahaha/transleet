# transleet
translate normal text to leet(l33t)

## Examples:
```python
print(transleet('the quick brown fox jumps over the lazy dog'))
# >>> '7h3 qu1ck 6r0wn f08 jump5 0v3r 7h3 l42y d09'
print(transleet('7h3 qu1ck 6r0wn f08 jump5 0v3r 7h3 l42y d09'))
# >>> 'the quick brown fox jumps over the lazy dog'

print(transleet('the quick brown fox jumps over the lazy dog', unicode=True, special=True))
# >>> '7#3 qµ1(κ 6γ0ωn ≠08 jµmρ5 0ν3γ 7#3 |42y δ09'
print(transleet('7#3 qµ1(κ 6γ0ωn ≠08 jµmρ5 0ν3γ 7#3 |42y δ09', unicode=True, special=True))
# >>> 'the quick brown fox jumps over the lazy dog'
```
