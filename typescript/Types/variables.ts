// Type Annotation

let movieTitle: string = 'Amadeus'
movieTitle = 'Arrival'
// movieTitle = 9
movieTitle.toUpperCase()

let numCatLives: number = 42
numCatLives = 60
numCatLives += 1
// numCatLives = 'Hello'

let gameOver: boolean = false
gameOver = true
// gameOver = 'true'

// Type Inference

let tvShow = 'Olive Kitteridge'
tvShow = 'The Other Two'
// tvShow = false

// the any type

let thing: any = 'hello'
thing = 1
thing = false
thing()
thing.toUpperCase()

// lazy initialization

const movies = ['Arrival', 'The Thing', 'Aliens', 'Amadeus']
let foundMovie: string
for (let movie of movies) {
  if (movie === 'Amadeus') {
    foundMovie = 'Amadeus'
  }
}
