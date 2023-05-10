$(document).ready(function() {
    $('form').on('submit', function(e){
        return false;
    });
  });

const togglepassword = document.getElementById('togglepassword');

togglepassword.addEventListener('click', function(e) {
    // toggle the type attribute
    const password = document.getElementById('validationDefaultPassword');
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

function validatePassword() {
  const password = document.getElementById("validationDefaultPassword");
  const passwordAlert = document.getElementById("password-alert");
  const requirements = document.querySelectorAll(".requirements");
  let lengBoolean, bigLetterBoolean, numBoolean, specialCharBoolean;
  let leng = document.querySelector(".leng");
  let bigLetter = document.querySelector(".big-letter");
  let num = document.querySelector(".num");
  let specialChar = document.querySelector(".special-char");
  const specialChars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~";
  const numbers = "0123456789";

  let value = password.value;
  if (value.length < 8) {
      lengBoolean = false;
  } else if (value.length > 7) {
      lengBoolean = true;
  }

  if (value.toLowerCase() == value) {
      bigLetterBoolean = false;
  } else {
      bigLetterBoolean = true;
  }

  numBoolean = false;
  for (let i = 0; i < value.length; i++) {
      for (let j = 0; j < numbers.length; j++) {
          if (value[i] == numbers[j]) {
              numBoolean = true;
          }
      }
  }

  specialCharBoolean = false;
  for (let i = 0; i < value.length; i++) {
      for (let j = 0; j < specialChars.length; j++) {
          if (value[i] == specialChars[j]) {
              specialCharBoolean = true;
          }
      }
  }

  if (lengBoolean == true && bigLetterBoolean == true && numBoolean == true && specialCharBoolean == true) {
      password.classList.remove("is-invalid");
      password.classList.add("is-valid");

      requirements.forEach((element) => {
          element.classList.remove("wrong");
          element.classList.add("good");
      });

  } else {
      password.classList.remove("is-valid");
      password.classList.add("is-invalid");


      if (lengBoolean == false) {
          leng.classList.add("wrong");
          leng.classList.remove("good");
      } else {
          leng.classList.add("good");
          leng.classList.remove("wrong");
      }

      if (bigLetterBoolean == false) {
          bigLetter.classList.add("wrong");
          bigLetter.classList.remove("good");
      } else {
          bigLetter.classList.add("good");
          bigLetter.classList.remove("wrong");
      }

      if (numBoolean == false) {
          num.classList.add("wrong");
          num.classList.remove("good");
      } else {
          num.classList.add("good");
          num.classList.remove("wrong");
      }

      if (specialCharBoolean == false) {
          specialChar.classList.add("wrong");
          specialChar.classList.remove("good");
      } else {
          specialChar.classList.add("good");
          specialChar.classList.remove("wrong");
      }
  }
}

(() => {
    'use strict'
    const form = document.querySelector('.needs-validation')
    const submitButton = document.getElementById('submitbutton')
    const remember = document.getElementById("remember");

    remember.addEventListener("change", () => {
      if (remember.classList.contains('is-valid')) {
        remember.classList.remove('is-valid')
      }
    });
  
    submitButton.addEventListener('click', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
  
        Array.from(form.elements).forEach(element => {
          if (element.checkValidity()) {
            element.classList.remove('is-invalid')
            element.classList.add('is-valid')
          } else {
            element.classList.remove('is-valid')
            element.classList.add('is-invalid')
          }

          validatePassword();

          if (remember.classList.contains('is-valid')) {
            remember.classList.remove('is-valid')
          }
        })


      } else {
        const password = document.getElementById("validationDefaultPassword");
        // If the password doesn't have the is-valid class, then it's invalid
        if (password.classList.contains('is-valid')) {
          submitWithData()
        }
      }

    }, false)
  
    // Add real-time validation as the user types
    Array.from(form.elements).forEach(element => {
      element.addEventListener('input', event => {
        if (element.checkValidity()) {
          element.classList.remove('is-invalid')
          element.classList.add('is-valid')
        } else {
          element.classList.remove('is-valid')
          element.classList.add('is-invalid')
        }
      })
    })
  
    // Function to submit the data when all fields are valid
    function submitWithData() {
      // Your code to submit the data goes here
      console.log('All fields are valid. Submitting the data...')

      // Submit the data to the server here. This is just a dummy form that doesn't actually submit.

      form.submit()
    }
  })()
  