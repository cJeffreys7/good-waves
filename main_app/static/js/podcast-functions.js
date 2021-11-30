const titleInput = document.querySelector("#id_title")
const descriptionInput = document.querySelector("#id_description")
const linkInput = document.querySelector("#id_link")
const imageInput = document.querySelector("#id_image")
const podcastImage = document.querySelector("#podcast-img")
const expression = /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/gi
const websiteRegEx = new RegExp(expression)

let linkPreviewDelay
let isDelayed = false

linkInput.addEventListener("input", generateLinkPreview)

function generateLinkPreview(){
  const inputText = linkInput.value
  // Determine if input is a valid web address
  if (inputText.match(websiteRegEx)) {
    // Interrupt api call delay if input is registered before delay finishes
    if (isDelayed) {
      interruptLinkPreviewDelay()
    }
    isDelayed = true
    linkPreviewDelay = setTimeout(function(){
      fetch(`https://api.linkpreview.net/?key=7c5dc8db90501ddb89b060074bcd94f3&q=${linkInput.value}`
      )
      .then(response => response.json())
      .then(data => {
        console.log(data)
        if (data.title) {
          titleInput.value = data.title
        }
        if (!data.description.includes('Invalid') && data.description) {
          descriptionInput.value = data.description.substring(0, 500)
        }
        if (data.image) {
          imageInput.value = data.image
          podcastImage.setAttribute('src', data.image)
        }
      })
      .catch(err => {
        console.log('Error:', err)
      })
    }, 1500)
  } else {
    // Stop api call if invalid web address is entered after a valid web address was previously entered
    if (isDelayed) {
      isDelayed = false
      interruptLinkPreviewDelay()
    }
  }
}

function interruptLinkPreviewDelay(){
  clearTimeout(linkPreviewDelay)
}