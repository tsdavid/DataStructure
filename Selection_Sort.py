"""
선택 정렬(selcetion_sort)
: 리스트에서 가장 작은 숫자를 선택, 앞쪽으로 옮기는 방법
: 전체 리스트에 있는 element들을 전부 찾아서 비교 후 정렬
  가장 작은 숫자를 선택
  test
"""


def selection_sort(a):  # 선택 정렬
    n = len(a)          # 인수로 받은 리스트의 길이
    # print(A)

    for i in range(n - 1):      # 0, 1, 2 ... n-2 
        least = i               # 최소 값 자릿 수 선정
        # print("print least : {} and A[least] : {}".format(least, A[least]))

        for j in range(i + 1, n):   # 최솟 값 자릿 수 이후로 loop 

            # print("print A[j] : {} < A[least] : {}".format(A[j], A[least]))
            if A[j] < A[least]:     # 대상 자리와 비교 연산
                least = j           # 최솟값 갱신시 자릿수 변화
                # print("LEAST HAS BEEN Changed.!!")

        A[i], A[least] = A[least], A[i]  # 배열 간 최솟값 교환
        printSteop(A, i+i)


def printSteop(arr, val):

    print("  Step %2d = " % val, end='')
    print(arr)


if __name__ == '__main__':

    A = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    print("Original : ", A)
    selection_sort(A)
    print("Selection : ", A)