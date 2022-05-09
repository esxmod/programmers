def solution(genres, plays):
    d = {}

    for i, genre in enumerate(genres):
        if genre not in d:
            d[genre] = plays[i]
        else:
            d[genre] += plays[i]

    v = []

    for genre, total in d.items():
        t = []

        for i, g in enumerate(genres):
            if g == genre:
                t.append((i, plays[i]))

        # 1. 재생 횟수, 2. 고유번호가 낮은 순
        t.sort(key=lambda x: (-x[1], x[0]))

        # 장르별 최대 2개의 고유번호만
        t = [a for a, b in t][:2]

        v.append((genre, total, t))

    v.sort(key=lambda x: -x[1])

    # flatten
    answer = sum([c for a, b, c in v], [])

    return answer


def test_case1():
    assert solution(["classic", "pop", "classic", "classic", "pop"],	[
                    500, 600, 150, 800, 2500]) == [4, 1, 3, 0]
