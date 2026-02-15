
/**
 * 치킨 배달
 */
import java.util.*;
import java.io.*;

public class Main {

    static int N, M;

    static int ans = Integer.MAX_VALUE; // 최솟값이기 때문에

    static class Point {
        int r, c;

        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    // static List<Point> selected = new ArrayList<>();
    static int[] selected;

    static List<Point> homes = new ArrayList<>();
    static List<Point> chickens = new ArrayList<>();

    // 맨해튼 거리 계산
    static int calc(Point a, Point b) {
        return Math.abs(a.r - b.r) + Math.abs(a.c - b.c);
    }

    // 치킨 집 중 M개 고르기 (조합)
    // 고른 치킨 집 인덱스를 저장?
    static void choose(int depth, int start) {
        if (depth == M) { // M 개 고르면 종료
            /**
             * 답을...알아네야하기 때문에
             */

            ans = Math.min(ans, calcTotal());

            return;

        }

        // for (int i = start; i <= M; i++) {
        for (int i = start; i < chickens.size(); i++) {
            selected[depth] = i; // 치킨집 인덱스 저장
            choose(depth + 1, i + 1);
        }

    }

    // 선택한 치킨 집으로 도시의 치킨 거리 계산 (총합)
    static int calcTotal() {
        int total = 0;
        for (Point home : homes) {
            int best = Integer.MAX_VALUE; // 최소 거리

            for (int idx : selected) {
                Point chicken = chickens.get(idx);
                best = Math.min(best, calc(chicken, home));
            }

            total += best;
        }
        // 가지치기
        if (total >= ans)
            return total;

        return total;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken()); // (2 ≤ N ≤ 50)
        M = Integer.parseInt(st.nextToken()); // (1 ≤ M ≤ 13)

        // 집 입력 받기
        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++) {
                int p = Integer.parseInt(st.nextToken());
                /**
                 * 0: 빈칸
                 * 1: 집
                 * 2: 치킨집
                 */
                if (p == 1) {
                    homes.add(new Point(r, c));
                } else if (p == 2) {
                    chickens.add(new Point(r, c));
                }
            }
        }

        // 최솟값
        selected = new int[M]; // M 개 고르기 때문에

        choose(0, 0);

        System.out.print(ans);

    }
}

/**
 * M이 1일 떄 예외...
 */