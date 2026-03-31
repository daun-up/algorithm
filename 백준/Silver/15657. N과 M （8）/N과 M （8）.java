
/**
 * N과 M (8)
 */
import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[] arr;
    static int[] output;
    static StringBuilder sb;

    static void choose(int idx, int cnt) {
        if (cnt == M) {
            for (int val : output) {
                sb.append(val).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = idx; i <= N; i++) {
            output[cnt] = arr[i];
            choose(i, cnt + 1);
        }

    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N + 1];
        output = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        choose(1, 0);

        System.out.println(sb);
    }
}
