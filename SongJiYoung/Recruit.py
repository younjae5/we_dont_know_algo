import sys
from operator import itemgetter, attrgetter

score = []
#신입사원 구하는 함수
def newRecruit():
    answer = 0
    #서류 성적을 기준으로 배열 정렬
    scoresort = sorted(score, key = itemgetter(0))
    #기준 설정 : 서류 성적 1등의 면접 성적
    passed = scoresort[0][1]
    answer += 1
    for a in range(1, len(scoresort)):
        #기준보다 성적이 낮으면 패스
        if scoresort[a][1] > passed:
            pass
        #기준보다 성적이 좋으면 기준 수정하고 채용
        else:
            passed = scoresort[a][1]
            answer = answer + 1
    return answer
if __name__ == '__main__':
    case = int(sys.stdin.readline())
    while case > 0:
        score = []
        recruit = []
        n = int(sys.stdin.readline())
        #입력
        for j in range(n):
            line = sys.stdin.readline()
            score.append(tuple(map(int, line.strip().split())))
        recruit = newRecruit()
        print(recruit)
        case = case - 1