
/**
 * 10819. 차이를 최대로
 */
import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[] arr;

    static boolean[] visited;
    static int[] perm;

    static int max;

    static void dfs(int depth) {
        if (depth == N) {
            int sum = 0;
            for (int i = 0; i < N - 1; i++) {
                sum += Math.abs(perm[i] - perm[i + 1]);
            }

            max = Math.max(sum, max);
            return;
        }

        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                perm[depth] = arr[i];

                dfs(depth + 1);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        max = 0;

        perm = new int[N];
        visited = new boolean[N];

        dfs(0);

        System.out.println(max);

    }
}
