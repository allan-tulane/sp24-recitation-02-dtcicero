from main import *
from main import compare_work

def test_simple_work():
  assert work_calc(10, 2, 2) == 50
  assert work_calc(20, 3, 2) == 240
  assert work_calc(30, 4, 2) == 1520
  assert simple_work_calc(5, 2, 2) == 25  
  assert simple_work_calc(15, 3, 2) == 405
  assert simple_work_calc(25, 3, 2) != 800
 

def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 20
  assert work_calc(20, 1, 2, lambda n: n * n) == 28764095
  assert work_calc(30, 3, 2, lambda n: n) == 65610
  assert work_calc(5, 2, 2, lambda n: 1) == 6  
  assert work_calc(15, 3, 2, lambda n: n) == 8760  
  assert work_calc(8, 2, 2, lambda n: n * n) == 1312


def test_compare_work():
  
  def t_compare_work(work_fn1, work_fn2):
      # Define values for n
      n_values = [10, 100, 1000]

      
      for n in n_values:
          result_fn1 = work_calc(n, 2, 2, work_fn1)
          result_fn2 = work_calc(n, 2, 2, work_fn2)

          print(f"For n={n}:")
          print(f"Work function 1: {result_fn1}")
          print(f"Work function 2: {result_fn2}")

          
          if result_fn1 > result_fn2:
              print("Work function 1 is greater.")
          elif result_fn1 < result_fn2:
              print("Work function 2 is greater.")
          else:
              print("Work functions are equal.")


  def work_fn1(n):
      return n**2  
  def work_fn2(n):
      return 2**n  

  t_compare_work(work_fn1, work_fn2)

test_compare_work()


def test_compare_span():
  
  def compare_span(span_fn1, span_fn2):
     
      n_values = [10, 100, 1000]

  
      for n in n_values:
          span_result_fn1 = span_calc(n, 2, 2, span_fn1)
          span_result_fn2 = span_calc(n, 2, 2, span_fn2)

          print(f"For n={n}:")
          print(f"Span function 1: {span_result_fn1}")
          print(f"Span function 2: {span_result_fn2}")

          if span_result_fn1 > span_result_fn2:
              print("Span function 1 is greater.")
          elif span_result_fn1 < span_result_fn2:
              print("Span function 2 is greater.")
          else:
              print("Span functions are equal.")

  def span_fn1(n):
      return n**2  

  def span_fn2(n):
      return 2**n  
  compare_span(span_fn1, span_fn2)

test_compare_span()