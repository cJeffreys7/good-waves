const firstNameInput = document.querySelector("#id_first_name")
const firstNameContainer = document.querySelector("tbody tr:first-child td")
const lastNameInput = document.querySelector("#id_last_name")
const lastNameContainer = document.querySelector("tbody tr:nth-child(2) td")
const usernameInput = document.querySelector("#id_username")
const usernameContainer = document.querySelector("tbody tr:nth-child(3) td")
const password1Input = document.querySelector("#id_password1")
const password1Container = document.querySelector("tbody tr:nth-child(4) td")
const password2Input = document.querySelector("#id_password2")
const password2Container = document.querySelector("tbody tr:nth-child(5) td")
const submitBtn = document.querySelector(".submit")
const firstNameToolTip = document.createElement("span")
const lastNameToolTip = document.createElement("span")
const usernameToolTip = document.createElement("span")
const password1ToolTip = document.createElement("span")
const password2ToolTip = document.createElement("span")

let validationDelay
let isDelayed = false
const delayRate = 500
submitBtn.disabled = true

firstNameInput.addEventListener('input', firstNameInputCheck)
lastNameInput.addEventListener('input', lastNameInputCheck)
usernameInput.addEventListener('input', usernameInputCheck)
password1Input.addEventListener('input', passwordInputCheck)
password2Input.addEventListener('input', passwordConfirmationCheck)

function firstNameInputCheck(){
  if (isDelayed) {
    interruptValidationDelay()
  }
  isDelayed = true
  validationDelay = setTimeout(function(){
    firstNameValidation(true)
    checkForm(false)
    isDelayed = false
  }, delayRate)
}

function lastNameInputCheck(){
  if (isDelayed) {
    interruptValidationDelay()
  }
  isDelayed = true
  validationDelay = setTimeout(function(){
    lastNameValidation(true)
    checkForm(false)
    isDelayed = false
  }, delayRate)
}

function usernameInputCheck(){
  if (isDelayed) {
    interruptValidationDelay()
  }
  isDelayed = true
  validationDelay = setTimeout(function(){
    usernameValidation(true)
    checkForm(false)
    isDelayed = false
  }, delayRate)
}

function passwordInputCheck(){
  if (isDelayed) {
    interruptValidationDelay()
  }
  isDelayed = true
  validationDelay = setTimeout(function(){
    passwordValidation(true)
    checkForm(false)
    isDelayed = false
  }, delayRate)
}

function passwordConfirmationCheck(){
  if (isDelayed) {
    interruptValidationDelay()
  }
  isDelayed = true
  validationDelay = setTimeout(function(){
    passwordConfirmationValidation(true)
    checkForm(false)
    isDelayed = false
  }, delayRate)
}

function firstNameValidation(showToolTip){
  if (!firstNameInput.value) {
    if (showToolTip) {
      firstNameToolTip.textContent = 'Please enter a first name'
      firstNameContainer.prepend(firstNameToolTip)
      firstNameToolTip.style.display = 'contents'
    }
    return false
  } else {
    if (showToolTip) {
      firstNameToolTip.style.display = 'none'
    }
    return true
  }
}

function lastNameValidation(showToolTip){
  if (!lastNameInput.value) {
    if (showToolTip) {
      lastNameToolTip.textContent = 'Please enter a last name'
      lastNameContainer.prepend(lastNameToolTip)
      lastNameToolTip.style.display = 'contents'
    }
    return false
  } else {
    if (showToolTip) {
      lastNameToolTip.style.display = 'none'
    }
    return true
  }
}

function usernameValidation(showToolTip){
  if (usernameInput.value) {
    const wordExpression = /[^\w@.+-]/g
    const usernameRegExp = new RegExp(wordExpression)
    if (usernameInput.value.match(usernameRegExp)) {
      if (showToolTip) {
        const invalidChars = new Set(usernameInput.value.match(usernameRegExp))
        let invalidCharStr = ""
        invalidChars.forEach(char => {
          invalidCharStr += `${char} `
        })
        usernameToolTip.textContent = `Cannot contain ${invalidCharStr} characters in username`
        usernameContainer.prepend(usernameToolTip)
        usernameToolTip.style.display = 'contents'
      }
      return false
    } else {
      if (showToolTip) {
        usernameToolTip.style.display = 'none'
      }
      return true
    }
  } else {
    if (showToolTip) {
      usernameToolTip.textContent = 'Please enter a user name'
      usernameContainer.prepend(usernameToolTip)
      usernameToolTip.style.display = 'contents'
    }
    return false
  }
}

function passwordValidation(showToolTip){
  if (password1Input.value) {
    if (password1Input.value.length >= 8) {
      const numericExpression = /^[0-9]*$/g
      const numericPasswordRegExp = new RegExp(numericExpression)
      if (password1Input.value.match(numericPasswordRegExp)) {
        if (showToolTip) {
          password1ToolTip.textContent = "Your password can't be entirely numeric"
          password1Container.prepend(password1ToolTip)
          password1ToolTip.style.display = 'contents'
        }
        return false
      } else {
        if (showToolTip) {
          password1ToolTip.style.display = 'none'
        }
        return true
      }
    } else {
      if (showToolTip) {
        password1ToolTip.textContent = 'Your password must contain at least 8 characters'
        password1Container.prepend(password1ToolTip)
        password1ToolTip.style.display = 'contents'
      }
      return false
    }
  } else {
    if (showToolTip) {
      password1ToolTip.textContent = 'Please enter a password'
      password1Container.prepend(password1ToolTip)
      password1ToolTip.style.display = 'contents'
    }
    return false
  }
}

function passwordConfirmationValidation(showToolTip){
  if (password2Input.value !== password1Input.value) {
    if (showToolTip) {
      password2ToolTip.textContent = 'Please enter the same password as before'
      password2Container.prepend(password2ToolTip)
      password2ToolTip.style.display = 'contents'
    }
    return false
  } else {
    if (showToolTip) {
      password2ToolTip.style.display = 'none'
    }
    return true
  }
}

function checkForm(showToolTip){
  let validated = true
  if (!firstNameValidation(showToolTip)) validated = false
  if (!lastNameValidation(showToolTip)) validated = false
  if (!usernameValidation(showToolTip)) validated = false 
  if (!passwordValidation(showToolTip)) validated = false
  if (!passwordConfirmationValidation(showToolTip)) validated = false
  if (validated) {
    console.log('Form is validated!')
    submitBtn.disabled = false
  } else {
    console.log('Form is invalid')
    submitBtn.disabled = true
    submitBtn.click()
  }
}

function interruptValidationDelay(){
  clearTimeout(validationDelay)
}