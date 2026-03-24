
/**
 * 2468. 안전 영역 (refactoring)
 */
import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[][] map;
    static boolean[][] visited;

    static int maxHeight;
    static int maxCnt; // 최대 안전 영역

    static int[] dr = { -1, 1, 0, 0 };
    static int[] dc = { 0, 0, -1, 1 };

    // 잠길 거 다 잠겼을 때 안전 영역을 세는 함수
    static void bfs(int r, int c, int h) {
        // 시작점 넣기
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] { r, c });
        visited[r][c] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();

            for (int d = 0; d < 4; d++) {
                int nr = cur[0] + dr[d];
                int nc = cur[1] + dc[d];

                if (inRange(nr, nc)) {
                    if (!visited[nr][nc] && map[nr][nc] > h) {
                        visited[nr][nc] = true;
                        queue.add(new int[] { nr, nc });
                    }
                }
            }
        }
    }

    static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < N;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        // 지역 초기화
        map = new int[N][N];

        int maxHeight = 0;
        // 지역의 높이 입력 받음
        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++) {
                map[r][c] = Integer.parseInt(st.nextToken());
                maxHeight = Math.max(map[r][c], maxHeight);
            }
        }

        maxCnt = 1;

        // 높이 1 부터 (maxHeight - 1) 까지 탐색
        for (int h = 1; h < maxHeight; h++) {
            visited = new boolean[N][N];
            int cnt = 0;
            // 전체 경우의 수 bfs 돌기
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    // 높이 h보다 크고, 아직 방문하지 않은 경우에만 bfs 시작
                    if (map[r][c] > h && !visited[r][c]) {
                        // 시작점 큐에 넣기
                        bfs(r, c, h);
                        cnt++;
                    }
                }
            }

            maxCnt = Math.max(cnt, maxCnt);
        }

        System.out.print(maxCnt);

    }
}

/**
 * 비의 양에 따라서 생기는 안전 영역의 최대 개수를 계산한다.
 * 비의 양의 경우는 Math.max(map)
 */