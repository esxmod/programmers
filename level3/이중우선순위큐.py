# 직접 구현해봐도 좋으나 우선순위 큐를 제공한다면
# 이 2개를 응용해서 구현할 수 있다.
import heapq


def solution(operations):
    max_heap = []
    min_heap = []  # heapq 의 기본은 최소힙
    size = 0

    for operation in operations:
        # 명령어 파싱
        command, value = operation.split(' ')
        value = int(value)

        if command == 'I':
            heapq.heappush(max_heap, -value)
            heapq.heappush(min_heap, value)
            size += 1
        # D 1
        elif value == 1 and max_heap:
            heapq.heappop(max_heap)
            size -= 1
        elif min_heap:
            heapq.heappop(min_heap)
            size -= 1

        if size <= 0:
            # 아래처럼 초기화 할 경우 메모리를 공유하게 되버림
            # max_heap = min_heap = []
            max_heap.clear()
            min_heap.clear()

    max_value = -max_heap[0] if max_heap and size > 0 else 0
    min_value = min_heap[0] if min_heap and size > 0 else 0

    return [max_value, min_value]


def test_case1():
    assert solution(["I 16", "D 1"]) == [0, 0]


def test_case2():
    assert solution(["I 7", "I 5", "I -5", "D -1"]) == [7, 5]


def test_case3():
    assert solution(["I 5", "I 2", "I 3", "D 1"]) == [3, 2]


def test_case4():
    assert solution(["I 5", "I 2", "I 3", "D -1"]) == [5, 3]


def test_case5():  # TC 1
    assert solution(["I 5", "I 4", "D 1", "D -1", "I 1", "I 2"]) == [2, 1]
