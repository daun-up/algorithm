#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;
    int cnt1 = 0;
    int cnt2 = 0;
    for (int i = 0; i < num_list.size(); i++){
            if (num_list[i] % 2 == 0) {
                cnt1 += 1;
            } else if(num_list[i] % 2 == 1) { cnt2 += 1;}
        }
    answer.push_back(cnt1);
    answer.push_back(cnt2);
    return answer;
}