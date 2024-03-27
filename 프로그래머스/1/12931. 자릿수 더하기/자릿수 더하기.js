function solution(n)
{
    var answer = 0;
    
    m = String(n);
    for (let i = 0; i < m.length; i++) {
        answer += parseInt(m[i]);
    }
    
    return answer;
}