from main import printStep
"""
삽입 정렬(Insertion Sort)
: 새로운 요소가 추가되면 재 정렬
  문제는 끼워넣어야 하는 케이스가 발생한다.
  그렇다면 끼워지는 기준 점 이후의 숫자들은 뒤로 한칸씩 밀려나갈것이다.
  그래서 맨 뒤쪽 항목부터 처리를 신경써야 한다.

"""


def insertion_sort(data):
    n = len(data)
    for i in range(1, n):  # 전체 looping
        # i : 현재 타겟 element aka 기준점
        # j : 기준점 이전 index
        j = i - 1
        # while loop를 통해 단일 요소에 대한 전체 탐색
        while 0 <= j and data[i] < data[j]:  # j가 인덱스 이고, i(현재 인덱스) 보다 j(이전 인덱스) 가 크다면
            data[j + 1] = data[j]  # 기점으로 모두 한칸씩 뒤로 밀림
            j -= 1
        data[j + 1] = data[i]   # 정렬을 위한 항목 삽입
        printStep(data, i)

if __name__ == '__main__':
    data = [5, 3, 8, 4,9,1,6,2,7]
    print("Original : " + data)
    insertion_sort(data)
    print("Insertion : " + data)



