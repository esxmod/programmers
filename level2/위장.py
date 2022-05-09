def solution(clothes):
    d = {}
    answer = 1

    # 같은 이름으로 주어지는 경우는 없다.
    for name, t in clothes:
        if t not in d:
            d[t] = 1
        d[t] += 1

    for num in d.values():
        answer *= num

    return answer - 1


def test_case1():
    assert solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], [
                    "green_turban", "headgear"]]) == 5


def test_case2():
    assert solution([["crowmask", "face"], ["bluesunglasses",
                    "face"], ["smoky_makeup", "face"]]) == 3
