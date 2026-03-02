
/**
 * 4179. 불! 내 힘으로 풀기
 */
import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static char[][] map;
    static Queue<int[]> fireQueue, jihunQueue;
    static boolean[][] jihunVisited;

    static int[] dr = { -1, 1, 0, 0 };
    static int[] dc = { 0, 0, -1, 1 };

    static boolean inRange(int r, int c) {
        return (r >= 0 && r < n && c >= 0 && c < m);
    }

    static void fire() {
        int size = fireQueue.size();
        for (int i = 0; i < size; i++) {
            int[] curr = fireQueue.poll();

            for (int d = 0; d < 4; d++) {
                int nr = curr[0] + dr[d];
                int nc = curr[1] + dc[d];

                // 불 확산
                if (inRange(nr, nc) && map[nr][nc] == '.') {
                    map[nr][nc] = 'F';
                    fireQueue.add(new int[] { nr, nc });
                }
            }
        }
    }

    static boolean bfs() {
        int size = jihunQueue.size();
        for (int i = 0; i < size; i++) {
            int[] curr = jihunQueue.poll();

            for (int d = 0; d < 4; d++) {
                int nr = curr[0] + dr[d];
                int nc = curr[1] + dc[d];

                // 탈출할 경우
                if (!inRange(nr, nc))
                    return true;
                // 이동 (범위 내이고, 방문한 적 없고, 지나갈 수 있을 때)
                if (inRange(nr, nc) && map[nr][nc] == '.' && !jihunVisited[nr][nc]) {
                    jihunVisited[nr][nc] = true;
                    jihunQueue.add(new int[] { nr, nc });
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new char[n][m];
        jihunVisited = new boolean[n][m];

        jihunQueue = new LinkedList<>();
        fireQueue = new LinkedList<>();
        for (int r = 0; r < n; r++) {
            String line = br.readLine();
            for (int c = 0; c < m; c++) {
                map[r][c] = line.charAt(c);

                if (map[r][c] == 'F') {
                    fireQueue.add(new int[] { r, c });
                }
                if (map[r][c] == 'J') {
                    jihunQueue.add(new int[] { r, c });
                    jihunVisited[r][c] = true;
                }
            }
        }

        int time = 0;
        String ans = "IMPOSSIBLE";
        while (!jihunQueue.isEmpty()) {
            time++;
            fire();
            if (bfs()) {
                ans = String.valueOf(time);
                break;
            }
        }

        System.out.println(ans);

    }
}
