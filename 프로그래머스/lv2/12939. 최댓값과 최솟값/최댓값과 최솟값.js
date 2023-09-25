// function solution(s) {
//     var answer = '';
//     let words = s.split(' ');
//     let numbers = words.map(Number)
//     numbers.sort();
//     console.log(numbers)
//     numbers.forEach((item) => {
//         if (item[i] < 0) {
            
//         }
//     })
//     return answer;
// }

function solution(s) {
    const tmp = s.split(" ");
    let max = +tmp[0]
    let min = +tmp[0];
    
    tmp.forEach(item => {
        if (+item < min) min = +item;
        if (+item > max) max = +item;
    })
    return `${min} ${max}`;
    
}