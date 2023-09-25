function solution(s){
    let answer = true;
    let count = 0;
    s.split("").forEach(item => {
        if (item == '(') count++;
        else count--;
        
        if (count < 0) answer = false;
    })
    return answer && count === 0;
    
}