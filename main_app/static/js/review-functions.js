const ratingStars = document.querySelectorAll(".rating-star")
const starRating = document.querySelector("#id_rating")

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

init()