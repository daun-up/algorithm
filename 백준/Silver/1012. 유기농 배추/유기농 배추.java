
/**
 * 1012. 유기농 배추
 */
import java.util.*;
import java.io.*;

public class Main {
    // 상 하 좌 우
    static int[] dr = { -1, 1, 0, 0 };
    static int[] dc = { 0, 0, -1, 1 };

    static int m, n, k;

    static int[][] map, visited;
    
    static boolean inRange(int nr, int nc){
        return (nr >= 0 && nr < n && nc >= 0 && nc < m);
    }

    static void bfs(int r, int c) {
        Queue<int[]> queue = new LinkedList<>(); // 좌표 (행, 열) 을 한 번에 넣기 위해
        queue.offer(new int[] { r, c });
        visited[r][c] = 1; // 시작점 방문 처리

        while (!queue.isEmpty()) {
            int[] curr = queue.poll(); // 현재 원소

            int currR = curr[0];
            int currC = curr[1];

            for (int d = 0; d < 4; d++) {
                int nr = currR + dr[d];
                int nc = currC + dc[d];

                // 배추이고, 방문하지 않았고, 범위 내
                if (inRange(nr, nc) && map[nr][nc] == 1 && visited[nr][nc] == 0) {
                    visited[nr][nc] = 1;
                    queue.offer(new int[] { nr, nc });
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            m = Integer.parseInt(st.nextToken()); // 배추밭 가로길이 (열)
            n = Integer.parseInt(st.nextToken()); // 세로 길이 (행)
            k = Integer.parseInt(st.nextToken()); // 배추 개수

            map = new int[n][m];
            visited = new int[n][m];

            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                map[y][x] = 1;
            }

            int cnt = 0;
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < m; c++) {
                    if(visited[r][c] == 0 && map[r][c] == 1){
                        bfs(r, c);
                        cnt++;
                    }
                }
            }

            System.out.println(cnt);
        }

    }
}
