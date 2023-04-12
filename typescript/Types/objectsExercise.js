var dune = {
    title: "Dune",
    originalTitle: "Dune Part One",
    director: "Denis Villeneuve",
    releaseYear: 2021,
    boxOffice: {
        budget: 165000000,
        grossUS: 108327830,
        grossWorldwide: 400671789,
    },
};
var cats = {
    title: "Cats",
    director: "Tom Hooper",
    releaseYear: 2019,
    boxOffice: {
        budget: 95000000,
        grossUS: 27166770,
        grossWorldwide: 73833348,
    },
};
// Write a function called getProfit that accepts a single Movie object
// It should return the movie's worldwide gross minus its budget
// For example...
// getProfit(cats) => -21166652
// function getProfit(movie: Movie): number {
//   return movie.boxOffice.grossWorldwide - movie.boxOffice.budget
// }
// function getProfit(movie: Movie): number {
//   const { grossWorldwide, budget } = movie.boxOffice
//   return grossWorldwide - budget
// }
function getProfit(_a) {
    var _b = _a.boxOffice, grossWorldwide = _b.grossWorldwide, budget = _b.budget;
    return grossWorldwide - budget;
}
console.log(getProfit(dune));
console.log(getProfit(cats));
