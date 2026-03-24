
/**
 * 2468. 안전 영역
 */
import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[][] map;
    static boolean[][] visited;
    static int maxHeight;
    static int cnt;
    static Queue<int[]> queue;
    static int maxCnt;

    static int[] dr = { -1, 1, 0, 0 };
    static int[] dc = { 0, 0, -1, 1 };

    // maxHeight 이하는 잠기게 하는 함수
    static void water(int height) {
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (map[r][c] <= height) {
                    map[r][c] = -1; // 물에 잠김
                }
            }
        }

    }

    // 잠길 거 다 잠겼을 때 안전 영역을 세는 함수
    static void bfs() {
        // queue 에 더 이상 없을 때
        cnt++;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();

            int cr = cur[0];
            int cc = cur[1];

            for (int d = 0; d < 4; d++) {
                int nr = cr + dr[d];
                int nc = cc + dc[d];

                if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                    if (!visited[nr][nc] && map[nr][nc] != -1) {
                        queue.add(new int[] { nr, nc });
                        visited[nr][nc] = true;
                    }
                }
            }
        }

    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        // 지역 초기화
        map = new int[N][N];

        maxHeight = 0;
        maxCnt = 1; // 아무 곳도 물에 잠기지 않았을 경우

        int[][] originalMap = new int[N][N];

        // 지역의 높이 입력 받음
        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++) {
                map[r][c] = Integer.parseInt(st.nextToken());
                maxHeight = Math.max(map[r][c], maxHeight);
            }
            originalMap[r] = map[r].clone();
        }

        queue = new LinkedList<>();

        for (int i = 1; i <= maxHeight; i++) {
            cnt = 0;
            visited = new boolean[N][N];
            water(i);
            // 전체 경우의 수 bfs 돌기
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    if (map[r][c] != -1 && !visited[r][c]) {
                        // 시작점 큐에 넣기
                        queue.add(new int[] { r, c });
                        bfs();
                    }
                }
            }

            maxCnt = Math.max(cnt, maxCnt);

            // map 초기화
            for (int r = 0; r < N; r++) {
                map[r] = originalMap[r].clone();
            }
        }

        System.out.print(maxCnt);

    }
}

/**
 * 비의 양에 따라서 생기는 안전 영역의 최대 개수를 계산한다.
 * 비의 양의 경우는 Math.max(map)
 */