
/**
 * 4256. 트리
 */
import java.util.*;
import java.io.*;

public class Main {

    static int[] preorder, inorder;
    static int p; // 전위 순회 훑는 인덱스

    static void solve(int p1, int p2) { // 탐색할 (서브) 트리 범위 [p1:p2]
        // 루트를 기준으로 왼/오 서브트리
        if (p1 > p2)
            return; // 함수 종료

        // int curRoot = preorder[p++]; // 0 번째 부터 root 를 시작하니까
        int root = preorder[p++];

        // 중위 순회에서 root 가 어디 있을까?
        int rootIdxInorder = 0;

        for (int i = p1; i <= p2; i++) {
            if (inorder[i] == root) {
                rootIdxInorder = i;
                break; // 반복문만 종료
            }
        }

        // 후위 순회 출력
        solve(p1, rootIdxInorder - 1);
        solve(rootIdxInorder + 1, p2);
        System.out.print(root + " ");

    }

    public static void main(String[] args) throws IOException {
        // System.setIn(new FileInputStream("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < T; tc++) {
            int n = Integer.parseInt(br.readLine()); // 트리 크기

            preorder = new int[n];
            inorder = new int[n];

            p = 0;

            // 전위 순회 입력
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                preorder[i] = Integer.parseInt(st.nextToken());
            }

            // root = preorder[0]; // root 노드 초기화

            // 중위 순회 입력
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                inorder[i] = Integer.parseInt(st.nextToken());
            }

            // inorder 에서 root 값인 인덱스 위치 찾고 전달
            // Q. inorder에서 해당 루트의 위치(idx) 어떻게 찾음?

            solve(0, n - 1);
            System.out.println();
        }
    }
}