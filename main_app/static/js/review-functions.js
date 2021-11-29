const ratingStars = document.querySelectorAll(".rating-star")
const starRating = document.querySelector("#id_rating")
const ratings = document.querySelectorAll(".review-rating")
const averageRating = document.querySelector("#podcast-avg-rating")
const numRatings = document.querySelector("#podcast-num-ratings")

ratingStars.forEach(star => {
  star.addEventListener("click", setStarFill)
})

function init(){
  starRating.value = 5
}

function setStarFill(evt){
  const rating = parseInt(evt.target.id.split('-')[1])
  starRating.value = rating
  ratingStars.forEach((star, idx) => {
    if (rating > idx) {
      star.style = "color: var(--star-fill);"
    } else {
      star.style = "color: lightgray;"
    }
  })
}

function calcAvgStarRating(){
  let newRating = parseInt(starRating.value)
  let ratingsAmount = parseInt(numRatings.dataset.numRatings)
  let ratingAverage = parseFloat(averageRating.dataset.avgRating)
  let avgRating = (ratingAverage * ratingsAmount + newRating) / (ratingsAmount + 1)
  averageRating.value = avgRating
}

init()