function solution(code) {
    var answer = '';
    let mode = 0;
    array = code.split("");
    for (let i = 0; i < array.length ; i++) {
        if (mode === 1) {
            if(array[i] == 1) {
                mode = 0;
            } else { // 1 이 아닐 때
                if(i % 2 !== 0) {
                    answer += array[i];
                }
            }
            
            
        } else { // mode === 0
            if(array[i] == 1){
                mode = 1;
            } else {
                if (i % 2 === 0) {
                    answer += array[i];
                }
            }
        } 
    }
    if (answer.length == 0) {
        return "EMPTY";
    } else {return answer;}
   
}