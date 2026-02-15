
/**
 * 1010. 다리 놓기
 */
import java.util.*;
import java.io.*;

public class Main {

    static int N, M;

    /**
     * 중복을 허용하지 않는 조합
     * 탐색 문제가 아니라 조합의 개수를 구하는 문제
     */

    // 메모이제이션 추가
    static long[][] memo = new long[31][31];

    static long comb(int n, int r) {
        if (r == 0 || r == n)
            return 1;
        if (memo[n][r] != 0)
            return memo[n][r];
        return memo[n][r] = comb(n - 1, r - 1) + comb(n - 1, r);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            long res = comb(M, N); // (0 < N ≤ M < 30)

            System.out.println(res);
        }
    }

}
