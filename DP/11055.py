import copy
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    A = list(map(int,sys.stdin.readline().split()))
    dp = [1 for _ in range(N)]
    dp = copy.deepcopy(A)
    for i in range(N):
        for j in range(i):
            if A[i]>A[j]:
                dp[i] = max(dp[i],dp[j]+A[i])
    print(max(dp))



"""
가장 큰 증가 부분 수열 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	30101	13668	10868	45.255%
문제
수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 합이 가장 큰 증가 부분 수열의 합을 출력한다.

예제 입력 1 
10
1 100 2 50 60 3 5 6 7 8
예제 출력 1 
113
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: gee308, gomyk12, mohana9
비슷한 문제
11053번. 가장 긴 증가하는 부분 수열
11054번. 가장 긴 바이토닉 부분 수열
11722번. 가장 긴 감소하는 부분 수열
12015번. 가장 긴 증가하는 부분 수열 2
12738번. 가장 긴 증가하는 부분 수열 3
14002번. 가장 긴 증가하는 부분 수열 4
14003번. 가장 긴 증가하는 부분 수열 5
알고리즘 분류
다이나믹 프로그래밍]"""