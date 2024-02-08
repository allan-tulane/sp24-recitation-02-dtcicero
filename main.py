"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):

  if n <= 1:
    return n

  return a * simple_work_calc(n // b, a, b) + n

def work_calc(n, a, b, f):

  if n <= 1:
      return f(n)

  
  return a * work_calc(n // b, a, b, f) + f(n)

def values_and_trends():
  
  print("f(n) = 1:")
  for n in [10, 100, 1000]:
      result = work_calc(n, 2, 2, lambda n: 1)
      print(f"W({n}) = {result}")

  
  print("\nf(n) = log n:")
  for n in [10, 100, 1000]:
      result = work_calc(n, 2, 2, lambda n: math.log2(n))
      print(f"W({n}) = {result}")

  
  print("\nf(n) = n:")
  for n in [10, 100, 1000]:
      result = work_calc(n, 2, 2, lambda n: n)
      print(f"W({n}) = {result}")





values_and_trends()

def span_calc(n, a, b, f):
  
  if n <= 1:
      return 0  

  span_recursive_calls = max(span_calc(n // b, a, b, f) 
                             for _ in range(a))
  span_current_level = f(n)

  return max(span_recursive_calls, span_current_level)



def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  result = []
  for n in sizes:
    # compute W(n) using current a, b, f
    result.append((
      n,
      work_fn1(n),
      work_fn2(n)
      ))
  return result
def print_results(results):
  
  print(tabulate.tabulate(results,
              headers=['n', 'W_1', 'W_2'],
              floatfmt=".3f",
              tablefmt="github"))



def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  """
  Compare the values of different recurrences for 
  given input sizes.

  Returns:
  A list of tuples of the form
  (n, work_fn1(n), work_fn2(n), ...)

  """
  result = []
  for n in sizes:
    # compute W(n) using current a, b, f
    result.append((
      n,
      span_fn1,
      span_fn2
      ))
  return result





