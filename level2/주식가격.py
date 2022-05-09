import collections


def solution(prices):

    # [1, 2, 3, 2, 3]
    #  1  1  1  1  1 | 4
    #     2  2  2  2 | 3
    #        3       | 0 (+1)
    #           2  2 | 1
    #              3 | 0

    # O(N^2) 로 풀어도 효율성을 통과한다.

    deque = collections.deque(prices)
    answer = []

    # 2중 for 문을 쓰는게 가장 보기 좋겠지만
    # 스택/큐를 굳이 쓰는 방법(?)
    # 단 pop(0) 은 효율성에서 시간 초과된다.
    while deque:  # len(deque) > 0
        count = 0
        # 맨 앞 요소를 기준으로
        current_price = deque.popleft()  # pop(0)

        # 나머지 주가들과 비교
        for price in deque:
            count += 1
            # 주가가 떨어진 시점
            if price < current_price:
                break

        answer.append(count)

    return answer


def test_case1():
    assert solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0]
