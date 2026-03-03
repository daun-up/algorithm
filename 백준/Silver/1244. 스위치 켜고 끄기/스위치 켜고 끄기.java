import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int students = Integer.parseInt(br.readLine());

        for (int i = 0; i < students; i++) {
            st = new StringTokenizer(br.readLine());

            int gender = Integer.parseInt(st.nextToken());
            int idx = Integer.parseInt(st.nextToken());

            // 만약 남자면
            if (gender == 1) {
                for (int j = 1; j <= n; j++) {
                    if (j % idx == 0) {
                        if (arr[j] == 1)
                            arr[j] = 0;
                        else
                            arr[j] = 1;
                    }
                }
            } else { // 여자이면
                // 1. 자기 자신은 무조건 바꿈
                arr[idx] = 1 - arr[idx];

                // 2. 대칭 검사 (범위 체크 필수!)
                for (int j = 1; idx - j >= 1 && idx + j <= n; j++) {
                    if (arr[idx - j] == arr[idx + j]) {
                        arr[idx - j] = 1 - arr[idx - j];
                        arr[idx + j] = 1 - arr[idx + j];
                    } else {
                        // 대칭이 깨지면 즉시 중단
                        break;
                    }
                }
            }

        }

        for (int i = 1; i <= n; i++) {
            System.out.print(arr[i] + " ");
            if (i % 20 == 0) { // 20번째마다 줄바꿈
                System.out.println();
            }
        }

    }

}
