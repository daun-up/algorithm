#include <string>
#include <vector>

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    int a = numer1 * denom2 + numer2 * denom1;
    int b = denom1 * denom2;
    int tmp = min(a,b);
    for (int i = 2; i <= tmp; i++){
        if (a % i == 0 && b % i == 0){
            a /= i;
            b /= i;
            tmp /= i;
            i = 1;
        }
    }
    vector<int> answer = { a, b };
    
    return answer;
}