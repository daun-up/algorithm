import java.util.*;
import java.io.*;
import java.math.BigInteger;

public class Main {
    static int N, K;
    static String[] nums;
    // 0~Z 각각을 Z로 바꿨을 때 얼마나 이득인지
    static BigInteger[] gain = new BigInteger[36];
    static final String BASE36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine().trim());
        nums = new String[N];
        for (int i = 0; i < N; i++)
            nums[i] = br.readLine().trim();
        K = Integer.parseInt(br.readLine().trim());

        Arrays.fill(gain, BigInteger.ZERO);

        // 전체 합 구하면서 gain도 같이 계산
        BigInteger sum = BigInteger.ZERO;
        for (int i = 0; i < N; i++) {
            sum = sum.add(to10(nums[i]));
        }

        // gain 상위 K개만큼 sum에 더해줌
        Arrays.sort(gain, Comparator.reverseOrder());
        for (int i = 0; i < K; i++) {
            sum = sum.add(gain[i]);
        }

        sb.append(to36(sum));
        System.out.print(sb);
    }

    // 36진수 -> 10진수 (gain 계산도 여기서 같이)
    static BigInteger to10(String s) {
        BigInteger result = BigInteger.ZERO;
        BigInteger place = BigInteger.ONE;
        BigInteger base = BigInteger.valueOf(36);

        for (int i = s.length() - 1; i >= 0; i--) {
            int d = BASE36.indexOf(s.charAt(i));
            result = result.add(BigInteger.valueOf(d).multiply(place));
            gain[d] = gain[d].add(BigInteger.valueOf(35 - d).multiply(place));
            place = place.multiply(base);
        }
        return result;
    }

    // 10진수 -> 36진수
    static String to36(BigInteger num) {
        if (num.equals(BigInteger.ZERO))
            return "0";

        StringBuilder sb = new StringBuilder();
        BigInteger base = BigInteger.valueOf(36);
        while (num.compareTo(BigInteger.ZERO) > 0) {
            BigInteger[] dr = num.divideAndRemainder(base);
            sb.append(BASE36.charAt(dr[1].intValue()));
            num = dr[0];
        }
        return sb.reverse().toString();
    }
}