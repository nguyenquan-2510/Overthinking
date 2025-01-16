"""
   19    2    104
lesson  ex     p
"""

n = int(input())
cond1 = n % 400 == 0
cond2 = n % 4 == 0 and n % 100 != 0
if cond1 or cond2: print("Nhuan")
else: print(" ?? ")