
class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        int INF = Integer.MAX_VALUE / 2;
        
        int[][] dist = new int[N + 1][N + 1]; // 1-based
        
        for(int i = 1; i <= N; i++){
            for(int j = 1; j <= N; j++){
                // 자기 자신에게로 가는 거리
                if(i == j) {dist[i][j] = 0;}
                else {dist[i][j] = INF;}
            }
        }
        
        for(int i = 0; i < road.length; i++){
            int s = road[i][0];
            int e = road[i][1];
            int w = road[i][2];
            
            // 양방향 그래프
            dist[s][e] = Math.min(dist[s][e], w);
            dist[e][s] = Math.min(dist[e][s], w);
            
        }
    
        for(int k = 1; k <= N; k++){
            for(int s = 1; s <= N; s++){
                for(int e = 1; e <= N; e++){
                    if(dist[s][k] + dist[k][e] < dist[s][e]){
                        // 가장 짧은 경로
                        // dist[s][e] = Math.min(dist[s][e], dist[s][k] + dist[k][e]);
                        dist[s][e] = dist[s][k] + dist[k][e];
                    }
                }
            }
        }
        

            for(int e = 1; e <= N; e++){
                if(dist[1][e] <= K) answer++;
            }
 
        

        return answer;
    }
}

// 출발지, 도착지, 가중치
// 양방향 그래프