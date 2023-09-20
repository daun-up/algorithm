function solution(number) {
    var answer = 0;
    let array = number.split("").map(Number);
    for (let i = 0; i < array.length; i++) {
        answer += array[i];
    }
    answer = answer % 9;
    return answer;
}