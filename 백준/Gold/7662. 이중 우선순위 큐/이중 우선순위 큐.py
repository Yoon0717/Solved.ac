'''
1. 최대값과 최소값을 관리하기 위해서 2개의 힙이 필요함
2. D 명령어마다 삭제를 진행해야 하는데, 힙은 루트 값 삭제만 보장함
3. 한쪽의 힙에서 루트 값을 삭제하면 다른 힙에서 무슨 값이 삭제 되어야 하는지 모호함
4. 따라서 uid로 관리하면서 삭제하는 값의 uid에 대한 alive 값을 처리
5. 해당 반복문이 끝날 때, 각 트리의 루트 값이 진짜 최대/최소 값인지 재확인
'''

import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()

T = int(input()) # 테스트 수
answer = []

for _ in range(T):
  k = int(input())
  min_heap = []
  max_heap = []
  alive = dict() # 삭제되었는지 확인용
  uid = 0 # 각 값마다 부여되는 고유번호
  
  def delete_min():
    while min_heap and not alive[min_heap[0][1]]: # root의 uid가 살아있는지
      heapq.heappop(min_heap)
  
  def delete_max():
    while max_heap and not alive[max_heap[0][1]]: # root의 uid가 살아있는지
      heapq.heappop(max_heap)
    
  for _ in range(k):
    operation, value = input().split()
    value = int(value)
    
    if operation == 'I':
      alive[uid] = True
      heapq.heappush(min_heap, (value, uid))
      heapq.heappush(max_heap, (-value, uid))
      uid += 1
    else: # operation == 'D'
      if value == 1:
        delete_max()
        if max_heap:
          _, id = heapq.heappop(max_heap)
          alive[id] = False
      else: # value == -1
        delete_min()
        if min_heap:
          _, id = heapq.heappop(min_heap)
          alive[id] = False
  # 마지막 하나가 남았을 경우, 둘 다 빼야함
  delete_max()
  delete_min()
  
  if not min_heap or not max_heap:
    answer.append('EMPTY')
  else:
    answer.append(f'{-max_heap[0][0]} {min_heap[0][0]}')

for a in answer:
  print(a)