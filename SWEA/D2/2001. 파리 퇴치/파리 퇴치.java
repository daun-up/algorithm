/**
 * 2001 파리퇴치(누적합)
 */
import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for(int test_case = 1; test_case <= T; test_case++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken()); 

            int[][] map = new int[n][n];


            for(int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine()); // 매 줄 초기화
                for(int j = 0; j < n; j++){
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            int maxSum = 0;

            // // 파리채를 옆으로 밀음
            // for(int i = 0; i <= n - m; i++){
            //     int currentSum = 0;
            //     // 첫 번째 윈도우(가장 위쪽 MxM)의 합 구하기
            //     for (int r = 0; r < n - m; r++){
            //         for(int c = i; c < i + m; c++){
            //             currentSum += map[r][c];
            //         }
            //     }
            //     maxSum = Math.max(maxSum, currentSum);
            // }
            
            for(int i = 0; i <= n - m; i++){
                for(int j = 0; j <= n - m; j++){
                    int currentSum = 0;

                    for(int r = i; r < i + m; r++){
                        for(int c = j; c < j + m; c++){
                            currentSum += map[r][c];
                        }
                    }

                    maxSum = Math.max(maxSum, currentSum);
                }
            }
            
            StringBuilder sb = new StringBuilder();
            sb.append("#").append(test_case).append(" ").append(maxSum);
            System.out.println(sb.toString());
        }
    }
}
