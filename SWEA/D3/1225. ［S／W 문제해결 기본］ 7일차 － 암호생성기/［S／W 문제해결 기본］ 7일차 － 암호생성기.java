/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
	public static void main(String args[]) throws Exception
	{
	
        Scanner sc = new Scanner(System.in);
        

        // 큐를 만들자!
        // 시간 제한은? 없는듯?

        // for (int test_case = 1; test_case <= T; test_case++) {
        while (sc.hasNextInt()) {
            
            int t = sc.nextInt();

            int[] arr = new int[8];

            for (int i = 0; i < 8; i++){
                arr[i] = sc.nextInt(); 
            }

            int cnt = 1;

            boolean isDone = false;
            // arr 에 0 이 있거나 0 보다 작아진다면 끝!
            // while (!isDone) {
                
            //     // while 문의 조건 확인 먼저
            //     for (int i = 1; i < arr.length; i++){
            //         if (arr[i] <= 0){
            //             isDone = true;
            //             break;
            //         }
            //         arr[arr.length - 1] = arr[0] - cnt;
            //         arr[i - 1] = arr[i];
            //         cnt ++;
            //     }
            // }

            while(!isDone){
                // 배열을 직접 수정하지 않기
                int first = arr[0] - cnt;

                if (first <= 0) {
                    // AI 추가
                    first = 0;
                    isDone = true;
                }

                for (int i = 0; i < 7; i++){
                    arr[i] = arr[i + 1];
                }

                arr[7] = first;
                cnt ++;
                if (cnt > 5) cnt = 1;
            }

                System.out.print("#" + t + " ");
                for (int j = 0; j < arr.length; j++) {
                    System.out.print(arr[j] + " ");
                }
                System.out.println();
        }
	}
}