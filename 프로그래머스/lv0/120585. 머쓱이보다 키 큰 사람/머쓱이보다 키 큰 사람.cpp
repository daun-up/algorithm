#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array, int height) {
    int answer = 0;
    int cnt1 = 0;
    for (int i = 0; i < array.size(); i++){
        if (height < array[i]){
            cnt1 += 1;
        }
    }
    answer = cnt1;
    return answer;
}