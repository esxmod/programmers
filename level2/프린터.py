def solution(priorities, location):
    # 기존의 순서를 기억하기 위해 index 추가
    tasks = [(priority, index) for index, priority in enumerate(priorities)]

    # 완료한 작업을 담을 공간
    done = []

    # Priority Queue, deque 를 사용하면 좋으나
    # 데이터가 최대 100개 밖에 없으므로 max, pop(0) 를 사용해도 문제 없어보인다.

    # 작업이 모두 완료될 때 까지 반복
    # 1개가 남는 경우 pop 처리를 하고나면 나머지 대기 작업이 없기 때문에 2이상인 경우로 처리한다.
    while(len(tasks) > 1):
        # 현재 뽑은 작업
        current_priority, current_index = tasks.pop(0)

        # 나머지 대기 작업 중 우선순위가 가장 높은값을 가져온다.
        # _ 는 unused value 의 의미 (pep8)
        max_priority, _ = max(tasks, key=lambda x: x[0])

        # 이 작업이 현재 작업보다 높으면 현재 작업을 제일 뒤로 보낸다.
        if current_priority < max_priority:
            tasks.append((current_priority, current_index))
        # 그렇지 않으면 현재 작업을 처리한다.
        else:
            done.append(current_index)

    # 남아있는 작업을 처리
    done.append(tasks[0][1])

    # 사실 모든 결과값을 다 알 필요가 없기 때문에 while 문 내에서 return 처리를 해도 된다.
    return done.index(location) + 1


def test_case1():
    assert solution([2, 1, 3, 2], 2) == 1


def test_case2():
    assert solution([1, 1, 9, 1, 1, 1], 0) == 5
