#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int i;

bool cmp(string s1, string s2) {
    if(s1[i] == s2[i]) {
        if(s1 < s2) return true;
        else return false;
    }
    else if(s1[i] < s2[i]){
        return true;
    }
    else return false;
}

vector<string> solution(vector<string> strings, int n) {
    i = n;
    vector<string> answer = strings;
    sort(answer.begin(), answer.end(), cmp);
    return answer;
}