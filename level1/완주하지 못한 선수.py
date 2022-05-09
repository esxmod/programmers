def solution(participant, completion):
    d = {}

    for k in participant:
        if k not in d:
            d[k] = 1
        else:
            d[k] += 1

    for k in completion:
        d[k] -= 1

    for k in participant:
        if d[k] > 0:
            return k


def test_case1():
    assert solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo"


def test_case2():
    assert solution(["marina", "josipa", "nikola", "vinko", "filipa"], [
        "josipa", "filipa", "marina", "nikola"]) == "vinko"


def test_case3():
    assert solution(["mislav", "stanko", "mislav", "ana"], [
        "stanko", "ana", "mislav"]) == "mislav"
