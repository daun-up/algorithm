// box: [가로, 세로, 높이] (단위: cm)
// n: 주사위 한 변의 길이 (단위: cm)

// 문제: 박스 안에 n x n x n 주사위를 최대 몇 개 넣을 수 있나요?
// 조건: 빈틈없이, 겹치지 않게
function solution(box, n) {
    const x = Math.floor(box[0] / n)
    const y = Math.floor(box[1] / n)
    const z = Math.floor(box[2] / n)
    return x * y * z;
}