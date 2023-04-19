class Player {
  static description = 'Player In Our Game' // Player.description
  #score = 0  // private property (과거에는 _score와 같이 썼지만 동작을 막지는 않았음)
  #numLives = 10

  constructor(first, last) {
    console.log('IN CONSTRUCTOR!')
    this.first = first
    this.last = last
    this.#secret()
  }

  static randomPlayer() {
    return new Player('Andy', 'Samberg')
  }

  get fullName() {
    return `${this.first} ${this.last}`
  }
  set fullName(newName) {
    const [first, last] = newName.split(' ')
    this.first = first
    this.last = last
  }

  get score() {
    return this.#score
  }
  set score(newScore) {
    if (newScore < 0) {
      throw new Error('Score must be positive!')
    }
    this.#score = newScore
  }

  // getScore() {
  //   return this.#score
  // }
  // updateScore(newScore) {
  //   this.#score = newScore
  // }
  getNumLives() {
    return this.#numLives
  }
  taunt() {
    console.log('BOOYAH!')
  }
  loselife() {
    this.#numLives -= 1
  }
  #secret() {
    console.log('SECRET!')
  }
}

class AdminPlayer extends Player {
  constructor(first, last, powers) {
    super()
    this.powers = powers
  }

  isAdmin = true
}

const admin = new AdminPlayer(["delete", "restore world"])
console.log('admin: ', admin)

const player1 = new Player('blue', 'steele')
// player1.taunt()
// console.log(player1.first)
// console.log(player1.last)
console.log(player1.fullName)
player1.fullName = 'Amy Adams'
console.log(player1.fullName)

console.log(player1.score)
player1.score = 320
console.log(player1.score)
// console.log(player1.getScore())
// player1.updateScore(28)
// console.log(player1.numLives)
// player1.loselife()
// console.log(player1.numLives)
console.log('player1: ', player1)

const player2 = new Player('charlie', 'brown')
// player2.taunt()
// console.log(player2.first)
// console.log(player2.last)
console.log('player2: ', player2)
