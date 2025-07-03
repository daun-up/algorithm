function solution(numbers) {
    // var answer = [];
    const answer = new Set();
    // 더할 수 있는 모든 수
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            answer.add(numbers[i] + numbers[j])
        }
    }
    return [...answer].sort((a,b) => a-b) ;
}