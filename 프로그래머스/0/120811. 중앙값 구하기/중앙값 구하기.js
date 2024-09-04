function solution(array) {
    // 오름차순으로 정렬
    array.sort(function(a,b){
        return a - b;
    });
    
    // 중앙값 계산
    var half = Math.floor(array.length / 2);
    return array[half];
} 
