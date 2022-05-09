# PriorityQueue 는 heapq 의 wrapper class 이다.
# 대신 전자는 Thread-safe 하기 때문에 다소 느리더라도 정확성이 검증된다.
# 하지만 코딩테스트 채점환경은 멀티스레딩 처리가 아니므로 heapq 를 쓰자
import heapq


def solution(scoville, K):
    answer = 0

    # 기존의 scoville 배열을 최소힙으로 변환
    # 여기서의 힙은 단순히 첫번째 원소가 최소값을 가지는 배열이다.
    heapq.heapify(scoville)

    # 현재 가장 낮은 값이 K 이상인 경우 종료
    while scoville[0] < K:

        # 만약 배열의 길이가 1이하면 더 이상 새로 만들 수 없음
        if len(scoville) < 2:
            answer = -1
            break

        # 스코빌 지수가 가장 낮은 두 개를 섞어 새로운 녀석을 만든다.
        tmp = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, tmp)
        answer += 1

    return answer


def test_case1():
    assert solution([1, 2, 3, 9, 10, 12], 7) == 2


# 만들 수 없는 경우
def test_case2():
    assert solution([1, 1, 1, 1], 100) == -1
