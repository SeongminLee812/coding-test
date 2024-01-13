
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[0:step] # 앞에서부터 step 만큼의 문자열 추출
        count = 1

        # step 크기만큼 증가 시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else: # 더이상 압축하지 못하는 경우 (다른 문자열이 나온 경우)
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 이전 상태 초기화
                count = 1 # count 초기화

        # 남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열 중 가장 짧은 것이 정답
        answer = min(answer, len(compressed))

    return answer




# =================================================

def solution(s):
    answer = len(s)
    # step만큼 늘려가면서 확인하기
    for step in range(1, len(s) // 2 + 1):
        prev = s[0:step]
        count = 1
        compressed = ''

        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else: # 달라지는 시점
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev

        answer = min(answer, len(compressed))

    return answer
