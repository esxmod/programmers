def solution(phone_book):
    # 길이 별로 딕셔너리 선언
    d = [{} for i in range(0, 20)]

    for num in phone_book:
        d[len(num) - 1][num] = 1

    for num in phone_book:
        k = len(num)
        # num 문자열 앞에서 부터 i 길이의 부분 문자열 생성 (1 ~ k-1)
        for i in range(1, k):
            if num[:i] in d[i - 1]:
                return False

    return True


def test_case1():
    assert solution(["119", "97674223", "1195524421"]) is False


def test_case2():
    assert solution(["123", "456", "789"]) is True


def test_case3():
    assert solution(["12", "123", "1235", "567", "88"]) is False
