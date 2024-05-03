function solution(s, n) {
    let answer = '';
    // 알파벳 필요
    // 대소문자 구분
    let upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let lower = 'abcdefghijklmnopqrstuvwxyz';
    
    // 공백은 아무리 밀어도 공백
    for (let i = 0; i < s.length; i++) {
        let text = s[i];
        if (text === ' ') {
            answer += ' ';
            continue
        }
        let textArr = upper.includes(text) ? upper : lower;
        let index = textArr.indexOf(text)+n;
        
        if (index >= textArr.length) {
            index -= textArr.length
        }
        answer += textArr[index];
    }
    return answer;
}