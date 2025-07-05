function solution(array) {
    var answer = 0;
    let map = new Map(); // 숫자별 등장 횟수를 저장할 Map 생성
    
    for (i of array) {
        map.set(i, (map.get(i) || 0) + 1) //  현재 값이 없다면 0, 있으면 기존 값에 +1
    }
    ar = [...map].sort((a,b) => b[1] - a[1])
    answer = ar.length === 1 || ar[0][1] > ar[1][1] ? ar[0][0] : -1
    // 최빈값이 유일한 경우 
    return answer;
}