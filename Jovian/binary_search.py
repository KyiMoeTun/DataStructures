!pip install jovian --upgrade --quiet

import jovian
from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3


tests = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
 {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
 {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
 {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
 {'input': {'cards': [6], 'query': 6}, 'output': 0},
 {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
 {'input': {'cards': [], 'query': 7}, 'output': -1},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
  'output': 7},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
   'query': 6},
  'output': 2}]

def test_location(cards, query, mid):
  mid_no = cards[mid]
  if mid_no == query:
    if mid-1 >=0 and cards[mid-1] == mid_no:
      return 'left'
    else:
      return 'found'
  elif mid_no < query:
    return 'left'
  else:
    return 'right'

def locate_card(cards, query):
  lo, hi = 0, len(cards) - 1
  while lo <= hi:
    mid = (lo+hi) // 2
    result = test_location(cards, query, mid)
    if result == 'found':
      return mid
    elif result == 'left':
      hi = mid - 1
    elif result == 'right':
      lo = mid + 1
  return -1

 evaluate_test_cases(locate_card, tests)