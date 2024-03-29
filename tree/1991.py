import sys

def preOrder(node):
    if node == '.':
        return
    print(node,end='')
    preOrder(tree[node][0])
    preOrder(tree[node][1])

def inOrder(node):
    if node == '.':
        return
    inOrder(tree[node][0])
    print(node,end='')
    inOrder(tree[node][1])
def postOrder(node):
    if node =='.':
        return
    postOrder(tree[node][0])
    postOrder(tree[node][1])
    print(node, end='')



if __name__ == "__main__":
    N = int(sys.stdin.readline())
    tree = {}
    for i in range(N):
        node,left,right = sys.stdin.readline().split()
        tree[node]=[left,right]
    preOrder('A')
    print()
    inOrder('A')
    print()
    postOrder('A')

""" 1991번
제출
맞힌 사람
숏코딩
재채점 결과
채점 현황
내 제출
 난이도 기여
강의
질문 검색
트리 순회 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	38178	24763	18899	65.956%
문제
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.



예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

예제 입력 1 
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
예제 출력 1 
ABDCEFG
DBAECFG
DBEGFCA
알고리즘 분류
트리
재귀"""