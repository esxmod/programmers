def solution(bridge_length, weight, truck_weights):
    # 문제 조건을 이해하기 다소 어려운데
    # bridge_length 가 다리 길이가 아닌 다리에 올라갈 수 있는 트럭 수로 나온다.
    # 이는 다리가 일차선이기 때문에 1자로 나열했다고 보면 된다.
    # 또한 두번째 예시(100, 100, [10])로 판단했을 때
    # 건너는 소요 시간을 다리 길이 + 1 초로 정의할 수 있다.

    # 다리가 먼저 들어가고 먼저 나가는 구조이므로
    # 이를 하나의 큐 라고 표현할 수 있다.

    # bridge_length 길이 만큼의 다리 생성
    bridge = [0] * bridge_length

    # 소요 시간
    answer = 0

    # truck: [7, 4, 5, 6]

    # 이동 방향 -->
    # 0 [0, 0]
    # 1 [7, 0]
    # 2 [0, 7]
    # 3 [4, 0]
    # 4 [5, 4]
    # 5 [0, 5]
    # 6 [6, 0]
    # 7 [6]
    # 8 []

    # 구현하는데 있어 이동 방향은 관계없고
    # queue 가 제일 적절하나 데이터가 많지 않은 관계상 list 로 구현함
    total_weight = 0

    # 다리위의 총 중량을 구할 때 매번 sum 을 처리하는 것 보다
    # 슬라이딩 윈도우 개념을 이용하여 처리하는 것이 효율적이다.
    while len(bridge):
        # 1. 나옴
        total_weight -= bridge.pop(0)  # shift

        # 2. 들어감

        # 지나가야할 트럭이 남아 있다면
        if len(truck_weights):
            # 다리위의 총 중량 + 들어갈 트럭 무게 <= 다리가 견딜 수 있는 무게인 경우
            if total_weight + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)  # shift
                total_weight += truck
                bridge.append(truck)
            # 트럭의 이동을 구현하기 위해 아래와 같이 무게가 0인 개념으로 처리한다.
            else:
                bridge.append(0)

        answer += 1

    return answer


def test_case1():
    assert solution(2, 10, [7, 4, 5, 6]) == 8


def test_case2():
    assert solution(100, 100, [10]) == 101


def test_case3():
    assert solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 110
