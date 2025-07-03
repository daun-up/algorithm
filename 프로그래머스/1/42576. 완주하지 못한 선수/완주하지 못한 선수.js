function solution(participant, completion) {
    const map = new Map();
    
    // 참가자 수 세기
    for (const name of participant) {
        map.set(name, (map.get(name) || 0) + 1)
    }
    
    // 완주자 수 세기
    for (const name of completion) {
        map.set(name, map.get(name) - 1)
    }
    
    // 3. 카운트가 0이 아닌 사람 찾기
    for (const [name, count] of map) {
        if (count > 0) return name;
    }
    
}