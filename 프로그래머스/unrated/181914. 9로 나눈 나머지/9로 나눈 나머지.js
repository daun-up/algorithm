function solution(number) {
    var answer = number.split("").map(Number);
    return answer.reduce((a, b) => a + b) % 9;
}