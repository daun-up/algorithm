
/**
 * 14502. 연구소
 */
import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[][] map;
    static int[] dx = { 0, 0, -1, 1 };
    static int[] dy = { -1, 1, 0, 0 };

    static int ans;

    static class Point {
        int r, c;

        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    // 벽 3개 세우는 조합
    static void backtracking(int depth) {
        if (depth == 3) {
            ans = Math.max(ans, bfs());
            return;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0) {
                    map[i][j] = 1;
                    backtracking(depth + 1);
                    map[i][j] = 0;
                }
            }
        }
    }

    // 상하좌우 탐색하면서 바이러스가 퍼뜨리기
    // 남은 안전 영역 개수 세기
    static int bfs() {
        int safe = 0;

        int[][] copy = new int[N][M];

        for (int i = 0; i < N; i++) {
            copy[i] = map[i].clone();
        }

        Queue<Point> q = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (copy[i][j] == 2) {
                    q.offer(new Point(i, j)); // 지금 바이러스가 있는 칸 큐에 넣기
                }
            }
        }

        // 바이러스 퍼뜨리기
        while (!q.isEmpty()) {
            Point cur = q.poll();

            for (int i = 0; i < 4; i++) {
                int nr = cur.r + dx[i];
                int nc = cur.c + dy[i];

                if (nr >= 0 && nr < N && nc >= 0 && nc < M) {
                    if (copy[nr][nc] == 0) {
                        copy[nr][nc] = 2;
                        q.offer(new Point(nr, nc));
                    }
                }
            }
        }

        // 안전 영역 세기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (copy[i][j] == 0) {
                    safe++;
                }
            }
        }

        return safe;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 격자 입력
        map = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        backtracking(0);
        System.out.print(ans);
    }
}
