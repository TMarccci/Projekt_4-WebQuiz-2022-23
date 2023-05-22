// Toggle Buttons Functionality

const togglepassword = document.getElementById('togglepassword1');
const togglepassword2 = document.getElementById('togglepassword2');
const togglepassword3 = document.getElementById('togglepassword3');

togglepassword.addEventListener('click', function(e) {
    // toggle the type attribute
    const password = document.getElementById('validationDefaultOldPass');
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

togglepassword2.addEventListener('click', function(e) {
    // toggle the type attribute
    const password = document.getElementById('validationDefaultNewPass1');
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

togglepassword3.addEventListener('click', function(e) {
    // toggle the type attribute
    const password = document.getElementById('validationDefaultNewPass2');
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});


// Edit password Functionality

const passNew1Input = document.getElementById('validationDefaultNewPass1');
const passNew2Input = document.getElementById('validationDefaultNewPass2');
const passOldInput = document.getElementById('validationDefaultOldPass');
const requirements = document.querySelectorAll(".requirements");
let lengBoolean, bigLetterBoolean, numBoolean, specialCharBoolean;
let leng = document.querySelector(".leng");
let bigLetter = document.querySelector(".big-letter");
let num = document.querySelector(".num");
let specialChar = document.querySelector(".special-char");
const specialChars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~";
const numbers = "0123456789";
var passwordAlert = document.getElementById('password-alert');
var firstTap = false;

// If focus on oldpassword set everything to invalid
passOldInput.addEventListener('focus', function() {
    if (firstTap == false) {
        passNew1Input.classList.remove("is-valid");
        passNew1Input.classList.add("is-invalid");
        passNew2Input.classList.remove("is-valid");
        passNew2Input.classList.add("is-invalid");
        passOldInput.classList.remove("is-valid");
        passOldInput.classList.add("is-invalid");

        // Update firstTap
        firstTap = true;
    }
    
}, false);

// Focus on first new input than show password criteria
passNew1Input.addEventListener('focus', function() {
    passwordAlert.classList.remove('d-none');
    validatePassword();
}, false);

passNew1Input.addEventListener("blur", () => {
    passwordAlert.classList.add("d-none");
});

// Typing checks
passNew1Input.addEventListener("input", () => {
    checkIfTheOldAndNewSame();
});

passNew2Input.addEventListener('input', () => {
    checkIfTheOldAndNewSame();
});

passOldInput.addEventListener('input', () => {
    checkIfTheOldAndNewSame();
});

function checkIfTheOldAndNewSame() {
    // If the old and new match set everything to invalid
    if (passOldInput.value == passNew1Input.value) {
        passNew1Input.classList.remove("is-valid");
        passNew1Input.classList.add("is-invalid");
        passNew2Input.classList.remove("is-valid");
        passNew2Input.classList.add("is-invalid");
        passOldInput.classList.remove("is-valid");
        passOldInput.classList.add("is-invalid");
    } else {
        // Check first if the old password is valid
        if (passOldInput.value.length >= 8) {
            passOldInput.classList.remove("is-invalid");
            passOldInput.classList.add("is-valid");
        }
        // Check if the new password is valid
        validatePassword();
        // Check if the new password is the same as the confirmation
        const pass1Value = passNew1Input.value;
        const pass2Value = passNew2Input.value;
        if (pass1Value === pass2Value && pass1Value != "" && pass2Value != "") {
            passNew2Input.classList.remove('is-invalid');
            passNew2Input.classList.add('is-valid');
        } else {
            passNew2Input.classList.remove('is-valid');
            passNew2Input.classList.add('is-invalid');
        }
    }
}

// Validates security criteria on passNew1Input
function validatePassword() {
    let value = passNew1Input.value;
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
        passNew1Input.classList.remove("is-invalid");
        passNew1Input.classList.add("is-valid");

        requirements.forEach((element) => {
            element.classList.remove("wrong");
            element.classList.add("good");
        });

    } else {
        passNew1Input.classList.remove("is-valid");
        passNew1Input.classList.add("is-invalid");

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

// Form submissionm, if all field valid then submit form
const form = document.getElementById('pwupdate');
form.addEventListener('submit', function(e) {
  e.preventDefault();

  // If valid
  const isPass1Valid = passNew1Input.classList.contains('is-valid');
  const isPass2Valid = passNew2Input.classList.contains('is-valid');
  const isPassOldValid = passOldInput.classList.contains('is-valid');

  if (isPass1Valid && isPass2Valid && isPassOldValid) {
    // Perform form submission or other actions
    console.log('Form submitted successfully');
    form.submit();
  } else {
    // Show an error message or perform other actions
    console.log('Form submission failed. Please check the password fields.');
  }
});

var form1submit = document.getElementById('submitbuttondataupdate');
form1submit.addEventListener('click', function(e) {
    var form1 = document.getElementById('dataupdate');
    if (form1.checkValidity() === false) {
        e.preventDefault();
        e.stopPropagation();
    }
    form1.classList.add('was-validated');
}, false);