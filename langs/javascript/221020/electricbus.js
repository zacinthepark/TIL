/*
  전기버스
  - A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
  - 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
  - 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
  - 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

  <입력>
    [
      3,   => 최대한 이동할 수 있는 정류장 수
      10,  => 종점 정류장 번호
      5,   => 설치된 충전기의 개수
      [1, 3, 5, 7, 9]  => 충전기가 설치된 정류장 번호
    ]

  <출력>
    현재 아래 주어진 입력에 따른 출력은
      3
      0
      4
    이다.
*/


// 입력
const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
  [10, 20, 5, [4, 7, 9, 14, 17]]  // 2 (추가 실험용 테케)
]


// 정답 풀이
function solution(K, N, M, chargers) {
  candidates = [0, ...chargers, N]
  let start = 0
  let ans = 0
  for (let i=1; i < candidates.length; i++) {
    // 충전소 간 거리가 K보다 큰 경우는 이동 불가
    if (candidates[i]-candidates[i-1] > K) {
      ans = 0
      break
    }
    // 시작지점에서 갈 수 있는 만큼 가고, 못가는 경우에 도달했을 때는 바로 전 충전소 지점에서 충전, 충전 횟수 1 증가
    if (candidates[i]-candidates[start] > K) {
      start = i-1
      ans++
    }
  }
  return ans
}


// 정답 출력
for (const input of inputs) {
  console.log(solution(...input))
}