class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;

        int left = 1;
        for(int i = 0; i < stations.length; i++){
            int curr = stations[i];
            int right = curr - w - 1;
            
            int cnt = right - left + 1;
            
            int range = w * 2 + 1;
            
            answer += (int)Math.ceil((double)cnt / range);
            // 12.35 * 10 반올림 / 10
            // 123.5 124.0 12.4
            // floor 내림
            left = curr + w + 1;
        }
        
        // 마지막 stations 의 오른쪽 처리
        int right = n;
        
        if(right >= left){
            int cnt = right - left + 1;
            int range = w * 2 + 1;
            answer += (int)Math.ceil((double)cnt / range);
        }
        
        return answer;
    }
}