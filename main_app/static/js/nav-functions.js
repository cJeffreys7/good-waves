const navIcons = document.querySelectorAll(".nav-icon")

function setActiveNavIcon(){
  let path = window.location.pathname
  navIcons.forEach(icon => {
    if (icon.id == path) {
      icon.classList.add("active-icon")
    }
  })
}

setActiveNavIcon()