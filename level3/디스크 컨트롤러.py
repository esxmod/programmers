import heapq


def solution(jobs):
    # 그리디하게 본다면
    # 작업 소요 시간이 짧은 순으로 먼저 처리하는 것이
    # 가장 평균시간이 단축될 것이라 예상된다.

    # 요점은 sort 를 하는 대신 최소힙으로 풀 수 있고
    # 이를 한번에 처리하는것 보다 시간을 기준으로 구간별로 나눠서 처리해내야 한다.

    total_time = 0  # 누적 시간
    start_time, end_time = -1, 0
    size, i = len(jobs), 0

    wait = []

    # ex)
    # (x) = start_time
    # [x] = end_time

    # 반례) 연속적인 작업이 아닌 경우
    # [0, 3], [500, 6], [1, 9]

    # [0, 3] => (0) + 3 => [3] - 0 => 3

    # (0) < 1 <= [3] 조건에 의해서 아래부터 처리
    # [1, 9] => (3) + 9 => [12] - 1 => 11

    # (3) < 500 <= [12] 조건이 안되므로 if not wait 로 처리
    # end_time 이 500 까지 확장되면 아래 처리
    # [500, 6] => (500) + 6 => [506] - 500 => 6

    # 반례) 동시간대의 작업이 존재하는 경우
    # [0, 10], [0, 10], [1, 1], [0, 10]

    # [0, 10] => (0) + 10 => [10] - 0 => 10
    # (0) < 1 < [10] 조건이 만족되어 [1, 1] 작업이 추가되고 최소힙에 의해 먼저 처리됨
    # [1, 1]  => (10) + 1 => [11] - 1 => 10
    # [0, 10] => (11) + 10 => [21] - 0 => 21
    # [0, 10] => (21) + 10 => [31] - 0 => 31

    # [0, 10], [0, 10], [1, 11], [0, 10]

    # [0, 10] => (0) + 10 => [10] - 0 => 10
    # (0) < 1 < [10] 조건이 만족되어 [1, 11] 작업이 추가되고 최소힙에 의해 맨 뒤로 보내짐
    # [0, 10] => (10) + 10 => [20] - 0 => 20
    # [0, 10] => (20) + 10 => [30] - 0 => 30
    # [1, 11] => (30) + 11 => [41] - 1 => 40

    # 총 size 길이만큼 if wait 구문 처리를 반복 수행
    while i < size:

        # 처리해야할 작업중에서
        for job in jobs:
            start, duration = job

            # 마지막 요청이 종료된 시간 이내에서 작업이 시작되는 경우는
            # 작업 소요시간이 짧은 순으로 연속적으로 수행하는 것이 최적이다.
            # 이전에 처리했던 작업이 중복되지 않도록 start_time < start 조건을 추가한다.
            if start_time < start <= end_time:
                heapq.heappush(wait, (duration, start))

        # 작업 소요시간이 짧은 순으로 처리
        # 이 때 이 작업들은 연속적이므로 아래와 같은 연산을 통해 처리 시간이 구해진다.
        # 동시간대에 들어오는 처리도 한번에 하나씩 처리된다.
        if wait:
            duration, start = heapq.heappop(wait)
            start_time = end_time
            end_time += duration
            total_time += (end_time - start)
            i += 1
        # 만약 위에서 연속적인 작업이 없다면 1초씩 end_time 을 확장해가며 구간을 탐색한다.
        # 이렇게 할 경우 큐가 비었을 때 먼저 요청이 들어온 작업 순으로 처리가 가능하다.
        else:
            end_time += 1

    return total_time // size


def test_case1():
    assert solution([[0, 3], [1, 9], [2, 6]]) == 9


def test_case2():
    assert solution([[0, 3], [1, 9], [500, 6]]) == 6


def test_case3():
    assert solution([[0, 1]]) == 1


def test_case4():
    assert solution([[1000, 1000]]) == 1000


def test_case5():
    assert solution([[0, 1], [0, 1], [0, 1]]) == 2


def test_case6():
    assert solution([[0, 10], [0, 10], [1, 1], [0, 10]]) == 18


def test_case7():
    assert solution([[0, 10], [0, 10], [1, 11], [0, 10]]) == 25


def test_case8():
    assert solution([[0, 1], [1000, 1000]]) == 500
