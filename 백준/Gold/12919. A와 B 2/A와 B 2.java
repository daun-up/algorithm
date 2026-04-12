// package BAEKJOON.src.B12919;

/**
 * A 와 B 2
 */

import java.util.*;
import java.io.*;

public class Main {
    static String S, T;
    static int result;

    static void dfs(String t) {
        if (t.length() == S.length()) {
            if (t.equals(S)) {
                result = 1;
            }
            return;
        }

        // 마지막 글자가 A -> 제거
        if (t.charAt(t.length() - 1) == 'A') {
            dfs(t.substring(0, t.length() - 1));
        }

        // 첫 번째 글자가 B -> 제거 후 뒤집음
        if (t.charAt(0) == 'B') {
            StringBuilder sb = new StringBuilder(t.substring(1));
            dfs(sb.reverse().toString());
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        S = st.nextToken();

        st = new StringTokenizer(br.readLine());
        T = st.nextToken();

        result = 0;

        dfs(T);

        System.out.print(result);
    }
}
