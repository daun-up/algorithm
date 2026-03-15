
/**
 * N과 M (1)
 */
import java.util.*;
import java.io.*;

public class Main {
    static int N, M;

    static int[] res;
    static boolean[] visited;

    static StringBuilder sb;

    static void choose(int depth) {
        if (depth == M) {
            // for (int i = 0; i < M; i++) {
            // System.out.print(res[i] + " ");
            // }
            for (int i : res)
                sb.append(i).append(" ");
            sb.append("\n");
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                res[depth] = i;
                choose(depth + 1);
                visited[i] = false;
            }
        }

    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        res = new int[M];
        visited = new boolean[N + 1];

        choose(0);

        System.out.print(sb);
    }
}

/**
 * 중복 없이 M 개를 고른 수열
 */