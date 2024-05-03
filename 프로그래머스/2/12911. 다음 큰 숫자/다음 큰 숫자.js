function count(n) {
    let count = 0;
    let binary = n.toString(2).split('');
    for (let i = 0; i < binary.length; i ++) {
        if(binary[i] == 1) count ++;
    }
    return count;
}

function solution(n) {
    let answer = n;
    while(true) {
        answer ++;
        if(count(answer) == count(n)) return answer;
    }
}