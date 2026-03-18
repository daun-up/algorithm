
/**
 * 유기농배추
 */
import java.util.*;
import java.io.*;

public class Main {
    static int T, M, N, K;
    static int[][] map;
    static boolean[][] visited;

    static int[] dr = { -1, 1, 0, 0 };
    static int[] dc = { 0, 0, -1, 1 };

    static int cnt;

    static void bfs(int r, int c) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] { r, c });

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cr = cur[0];
            int cc = cur[1];
            visited[cr][cc] = true;

            for (int i = 0; i < 4; i++) {
                int nr = cr + dr[i];
                int nc = cc + dc[i];

                if (nr >= 0 && nr < M && nc >= 0 && nc < N && !visited[nr][nc] && map[nr][nc] == 1) {
                    visited[nr][nc] = true;
                    q.offer(new int[] { nr, nc });
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());

        for (int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());
            cnt = 0;

            map = new int[M][N];
            visited = new boolean[M][N];
            // for (int r = 0; r < M; r++) {
            // st = new StringTokenizer(br.readLine());
            // for (int c = 0; c < N; c++) {
            // map[r][c] = Integer.parseInt(st.nextToken());
            // }
            // }
            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                int r = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                map[r][c] = 1;
            }

            for (int r = 0; r < M; r++) {
                for (int c = 0; c < N; c++) {
                    if (map[r][c] == 1 && !visited[r][c]) { // 배추 있고 방문 안 했을 때
                        bfs(r, c);
                        cnt++;
                    }
                }
            }

            System.out.println(cnt);
        }

    }
}