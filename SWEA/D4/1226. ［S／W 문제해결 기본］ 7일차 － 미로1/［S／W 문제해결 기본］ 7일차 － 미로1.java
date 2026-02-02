/**
 * 1226 미로 1 (bfs)
 */
import java.io.*;
import java.util.*;

public class Solution {
    static int[][] map;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
      
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = 10;

        for(int test_case = 0; test_case < T; test_case++){
            int n = Integer.parseInt(br.readLine());

            map = new int[16][16];
            visited = new boolean[16][16];

            int s = 0;
            int e = 0;

            for(int i = 0; i < 16; i++){
                String line = br.readLine();

                for(int j = 0; j < 16; j++){
                    map[i][j] = line.charAt(j) - '0';
                    if(map[i][j] == 2){
                        s = i;
                        e = j;
                    }
                }
            }
            // System.out.print('#' + test_case + " " + bfs(s, e));
            int result = bfs(s, e);
            System.out.println("#" + n + " " + result);

        }
    }
    public static int bfs(int s, int e){
        Queue<int[]> queue = new LinkedList<>();

        queue.add(new int[] {s, e});
        visited[s][e] = true;

        while(!queue.isEmpty()){
            int[] cur = queue.poll(); // 현재 좌표
            int cx = cur[0];
            int cy = cur[1];

            for(int i = 0; i < 4; i++){
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if(nx >= 0 && nx < 16 && ny >= 0 && ny < 16){
                    if(map[nx][ny] == 3) return 1;

                    if(map[nx][ny] == 0 && !visited[nx][ny]){
                        visited[nx][ny] = true;
                        queue.add(new int[]{nx, ny});
                    }
                }
            }
        }
        return 0;
    }
}

