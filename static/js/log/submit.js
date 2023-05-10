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

(() => {
    'use strict'
    const form = document.querySelector('.needs-validation')
    const submitButton = document.getElementById('submitbutton')
  
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
        })

      } else {
        submitWithData()
      }

    }, false)
  
    // Function to submit the data when all fields are valid
    function submitWithData() {
      // Your code to submit the data goes here
      console.log('All fields are valid. Submitting the data...')

      // To-Do LOG USER IN

      form.submit()
    }
  })()
  