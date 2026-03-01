
/**
 * 알파벳
 */
import java.util.*;
import java.io.*;

public class Main {
    static int r, c, maxDist;
    static char[][] board;

    // 상하좌우
    static int[] dr = { -1, 1, 0, 0 };
    static int[] dc = { 0, 0, -1, 1 };

    // static boolean[][] visited;
    static boolean[] alphabet = new boolean[26]; // 알파벳 중복 체크 용
    // 체크할 때 알파벳을 배열의 인덱스러 매핑하여 저장

    static void backtracking(int row, int col, int cnt) {

        // 현재 칸까지 거리로 최댓값 갱신
        maxDist = Math.max(maxDist, cnt);

        for (int i = 0; i < 4; i++) {
            int nr = row + dr[i];
            int nc = col + dc[i];

            if (nr >= 0 && nr < r && nc >= 0 && nc < c) {
                int nextIdx = board[nr][nc] - 'A';

                if (!alphabet[nextIdx]) {
                    alphabet[nextIdx] = true;
                    backtracking(nr, nc, cnt + 1);
                    alphabet[nextIdx] = false;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        board = new char[r][c];
        for (int i = 0; i < r; i++) {
            String line = br.readLine();
            for (int j = 0; j < c; j++) {
                board[i][j] = line.charAt(j);
            }
        }

        alphabet[board[0][0] - 'A'] = true;
        backtracking(0, 0, 1);
        System.out.print(maxDist);

    }
}
