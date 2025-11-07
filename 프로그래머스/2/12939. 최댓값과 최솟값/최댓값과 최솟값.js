function solution(s) {
    // var answer = '';
    var answer = s.split(' ')
    var min = Math.min(...answer)
    var max = Math.max(...answer)
    // return answer;
    return min + " " + max;
}