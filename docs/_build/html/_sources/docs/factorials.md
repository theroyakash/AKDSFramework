# Factorials
Factorials are very simple things. They're just products, indicated by an exclamation mark. For instance, "four factorial" is written as $4!$ and means $1×2×3×4 = 24$. In general, $n!$ ("enn factorial") means the product of all the whole numbers from $1$ to $n$. That is, 

$$n! = 1×2×3×...×n$$

So we provide a very easy interface to calculate the factorial for a given number.
```python
from AKDSFramework.applications import factorials

print(factorials(5))
```
## Couple of ways to calculate
Now there are two ways to calculate the factorial for a given number, one using a recursive call to calculate the factorial another using iterative method. By default when you don't mention anything it'll use a iterative method to calculate. To explicitly tell the program to calculate the factorial with recursive call you need to pass an argument `iteratively` as False like this

```python
from AKDSFramework.applications import factorials

print(factorials(5, iteratively=False))
```