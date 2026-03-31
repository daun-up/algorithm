
/**
 * N과 M (9)
 */
import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[] arr;
    static int[] output;
    static StringBuilder sb;
    static boolean[] visited;

    static void choose(int idx, int cnt) {
        if (cnt == M) {
            for (int val : output) {
                sb.append(val).append(" ");
            }
            sb.append("\n");
            return;
        }

        int flag = 0;

        for (int i = 1; i <= N; i++) {
            if (!visited[i] && arr[i] != flag) {
                visited[i] = true;
                output[cnt] = arr[i];
                flag = arr[i];
                choose(i + 1, cnt + 1);
                visited[i] = false;
            }
        }

    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();

        // 입력
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 전역 변수 초기화
        arr = new int[N + 1];
        output = new int[M];
        visited = new boolean[N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        choose(1, 0);

        System.out.println(sb);
    }
}
