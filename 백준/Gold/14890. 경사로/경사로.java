
/**
 * 경사로
 */
import java.util.*;
import java.io.*;

public class Main {
    static int n, l;
    static int[][] map;

    static boolean findR(int idx) {
        int[] path = new int[n];
        boolean[] visited = new boolean[n]; // 경사로 설치 여부

        // 이번에 검사하는 길
        for (int i = 0; i < n; i++) {
            path[i] = map[idx][i];
        }

        // 경사로 설치할지 말지 고민 중
        for (int i = 0; i < n - 1; i++) {
            if (path[i] == path[i + 1])
                continue; // 높이가 같으면 통과

            int diff = path[i] - path[i + 1];

            if (Math.abs(diff) > 1)
                return false; // 차이가 1 보다 크면 실패

            if (diff == 1) { // 내리막 (현재 > 다음)
                // i+1부터 L개의 칸에 경사로 설치
                for (int j = i + 1; j <= i + l; j++) {
                    // 범위 밖이거나, 이미 설치됐거나, 높이가 낮은 쪽(path[i+1])과 다르면 실패
                    // 기준이 되는 높이는 낮은 쪽이어야 함
                    if (j >= n || visited[j] || path[j] != path[i + 1])
                        return false;
                    visited[j] = true;
                }
            } else if (diff == -1) { // 오르막 (현재 < 다음)
                // i부터 뒤로 L개의 칸에 경사로 설치
                for (int j = i; j > i - l; j--) {
                    // 범위 밖(0미만)이거나, 이미 설치됐거나, 높이가 낮은 쪽(path[i])과 다르면 실패
                    if (j < 0 || visited[j] || path[j] != path[i])
                        return false;
                    visited[j] = true;
                }
            }
        }

        return true;
    }

    static boolean findC(int idx) {
        int[] path = new int[n];
        boolean[] visited = new boolean[n]; // 경사로 설치 여부

        // 이번에 검사하는 길
        for (int i = 0; i < n; i++) {
            path[i] = map[i][idx];
        }

        // 경사로 설치할지 말지 고민 중
        for (int i = 0; i < n - 1; i++) {
            if (path[i] == path[i + 1])
                continue; // 높이가 같으면 통과

            int diff = path[i] - path[i + 1];

            if (Math.abs(diff) > 1)
                return false; // 차이가 1 보다 크면 실패

            if (diff == 1) { // 내리막 (현재 > 다음)
                // i+1부터 L개의 칸에 경사로 설치
                for (int j = i + 1; j <= i + l; j++) {
                    // 범위 밖이거나, 이미 설치됐거나, 높이가 낮은 쪽(path[i+1])과 다르면 실패
                    // 기준이 되는 높이는 낮은 쪽이어야 함
                    if (j >= n || visited[j] || path[j] != path[i + 1])
                        return false;
                    visited[j] = true;
                }
            } else if (diff == -1) { // 오르막 (현재 < 다음)
                // i부터 뒤로 L개의 칸에 경사로 설치
                for (int j = i; j > i - l; j--) {
                    // 범위 밖(0미만)이거나, 이미 설치됐거나, 높이가 낮은 쪽(path[i])과 다르면 실패
                    if (j < 0 || visited[j] || path[j] != path[i])
                        return false;
                    visited[j] = true;
                }
            }
        }

        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken()); // 경사로의 길이

        map = new int[n][n];

        for (int r = 0; r < n; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < n; c++) {
                map[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        // 탐색 순서를 어떻게 해야 하지?
        // 행 먼저 돌려
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (findR(i))
                count++; // 행
            if (findC(i))
                count++; // 열
        }

        System.out.print(count);

    }
}
