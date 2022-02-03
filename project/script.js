"use strict";

let numberOfFilms = prompt("Сколько фильмов вы уже посмотрели?", "");

let personalMovieDb = {
    count : `${numberOfFilms}`,
    movies : {},
    actors : {},
    genres : [],
    privat : false
};

let firstMovie = prompt("Один из просмотренных недавно фильмов?", "");
let firstRating = prompt("Насколько оцените его?","");
let secondMovie = prompt("Один из просмотренных недавно фильмов?", "");
let secondRating = prompt("Насколько оцените его?","");

personalMovieDb.movies[`${firstMovie}`] = `${firstRating}`;
personalMovieDb.movies[`${secondMovie}`] = `${secondRating}`;

console.log(personalMovieDb);