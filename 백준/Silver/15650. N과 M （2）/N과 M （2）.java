
/**
 * N과 M (2)
 */
import java.util.*;
import java.io.*;

public class Main {
    static int[] pick;
    static int N, M;
    static StringBuilder sb = new StringBuilder();

    // depth: 현재까지 뽑은 개수
    // start: 다음에 선택할 최소 숫자
    // static void backtracking(int depth, int start) {
    // // M개 다 고르면 출력
    // if (depth == M) {
    // for (int i = 0; i < M; i++) {
    // sb.append(pick[i]).append(" ");
    // }

    // return;
    // }

    // for (int i = start; i <= N; i++) {
    // pick[depth] = i;
    // backtracking(depth + 1, i + 1);
    // }

    // }

    static void dfs(int depth, int start) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                sb.append(pick[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = start; i <= N; i++) {
            pick[depth] = i;
            dfs(depth + 1, i + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        /**
         * NCM
         * 오름차순
         */
        pick = new int[M];

        // backtracking(0, 1);
        dfs(0, 1);

        System.out.print(sb);

    }
}
