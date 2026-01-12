import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입력을 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            // 종료 조건
            if (n == 0 && k == 0) break;

            int[] nodes = new int[n];
            int k_idx = 0;
            
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                nodes[i] = Integer.parseInt(st.nextToken());
                if (nodes[i] == k) {
                    k_idx = i; // k의 위치(인덱스) 미리 저장
                }
            }

            int[] parent_idx = new int[n];
            Arrays.fill(parent_idx, -1); // 부모 배열을 -1로 초기화
            
            int cur_parent_idx = -1;
            
            // 1. 부모 인덱스 설정
            for (int i = 1; i < n; i++) {
                if (nodes[i] != nodes[i - 1] + 1) {
                    cur_parent_idx++;
                }
                parent_idx[i] = cur_parent_idx;
            }

            // 2. 사촌 찾기
            int k_parent = parent_idx[k_idx];
            int ans = 0;
            
            // k가 루트가 아니고(-1), 할아버지가 존재할 때(parent_idx[k_parent] != -1)만 실행
            if (k_parent != -1 && parent_idx[k_parent] != -1) {
                int k_grandparent = parent_idx[k_parent];
                
                for (int i = 1; i < n; i++) {
                    // 부모는 다르고, 할아버지는 같은 경우
                    if (parent_idx[i] != k_parent) {
                        // parent_idx[i]가 -1이면 할아버지를 찾을 때 에러가 날 수 있으므로 체크
                        if (parent_idx[i] != -1 && parent_idx[parent_idx[i]] == k_grandparent) {
                            ans++;
                        }
                    }
                }
            }
            
            System.out.println(ans);
        }
    }
}