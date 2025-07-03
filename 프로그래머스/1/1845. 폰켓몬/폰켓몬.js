function solution(nums) {
    var answer = 0;
    const max = nums.length / 2;
    const tmp = new Set();
    
    // 최대한 많은 종류의 포켓몬을 챙겨야함
    for (const pocketmon of nums) {
        tmp.add(pocketmon)
    }
    
    
    return Math.min(tmp.size, max);
}