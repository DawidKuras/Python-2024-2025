import math
import keyword

print("\nFunkcje w module math:")
print([func for func in dir(math) if callable(getattr(math, func))])

print("\nFunkcje w module keyword:")
print([func for func in dir(keyword) if hasattr(keyword, func) and callable(getattr(keyword, func))])

print("\nFunkcje w module tuple (wbudowany):")
print([func for func in dir(tuple) if callable(getattr(tuple, func))])