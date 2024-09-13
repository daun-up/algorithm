function solution(n) {
    var answer = 0;
    const array = n.toString().split("").map(Number)
    array.sort()
    array.reverse()
    answer = Number(array.join(""))
    return answer;
}