function solution(code) {
    var answer = '';
    let mode = 0;
    for (let i = 0; i < code.length ; i++) {
        if (mode === 1) {
            if(code[i] == 1) {
                mode = 0;
            } else { // 1 이 아닐 때
                answer = i%2 === 0 ? answer : answer + code[i];
            }
        } else { // mode === 0
            if(code[i] == 1){
                mode = 1;
            } else {
                answer = i%2 === 0 ? answer + code[i] : answer;
            }
        } 
    }
    
    return answer.length === 0 ? "EMPTY" : answer;
}