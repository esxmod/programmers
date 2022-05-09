def solution(progresses, speeds):
    remains = []

    # 각 작업이 완료되기 까지 남은 일수
    # for i, progress in enumerate(progresses): 에서 speeds[i] 로 참조해도 되나
    # zip 을 통해 동시에 여러 객체를 순회할 수 있다.
    for progress, speed in zip(progresses, speeds):
        # 남은 일수 = (100 - 현재 작업 진도) / 작업 속도
        # 단 소수점은 무조건 올림처리 해야한다.
        # import math 를 통해 math.ceil 를 호출해도 되나
        # // 연산자가 기본적으로 소수점을 버림이 아닌 내림인 점을 이용할 수 있다.
        remains.append(-(-(100 - progress) // speed))

    answer = []

    # queue, deque 을 쓰는게 가장 좋고
    # 리스트에서 pop(0) 으로도 처리 가능하다. (데이터가 많은 경우 성능 저하)
    # 가능하면 성능을 위해 데이터를 수정하지 않고 참조만 하는 방법을 써보자
    current = remains[0]
    count = 1

    remains.append(1e9)

    # 앞의 기능부터 처리를 하고, 만약 다음 기능들이 이미 완성되었을 경우 함께 내보낸다.
    # 7 3 9 1e9
    # 5 10 1 1 20 1 1e9
    for remain in remains[1:]:
        if current >= remain:
            count += 1
        else:
            answer.append(count)
            count = 1
            current = remain

    return answer


def test_case1():
    assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]


def test_case2():
    assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]
