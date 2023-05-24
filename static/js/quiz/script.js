const privatequiz = document.getElementById('private');
const publicquiz = document.getElementById('public');
const apperainsearch = document.getElementById('appearinsearch');

privatequiz.addEventListener('click', () => {
    // Disable appear in search
    apperainsearch.checked = false;
    apperainsearch.disabled = true;
}, false);

publicquiz.addEventListener('click', () => {
    // Enable appear in search
    apperainsearch.disabled = false;
}, false);

const cardnumber = document.getElementById('cardnumber');
const addcard = document.getElementById('addcard');
const cardlist = document.getElementById('cardslist');

addcard.addEventListener('click', () => {
    cardnumber.innerHTML = parseInt(cardnumber.innerHTML) + 1;

    // Get current card number
    const i = parseInt(cardnumber.innerHTML)-1;

    // Add card to cardlist
    const card = document.createElement('div');
    card.classList.add('flashcard');
    card.id = `flashcard${ i }`;
    card.innerHTML = `
    <div class="col-12">
        <div class="row">
            <div class="col-auto justify-content-center align-items-center">
                <div class="h5" style="margin-top: 5px;">${ i+1 }. kártya</div>
            </div>
            <div class="col-2">
                <button type="button" class="btn btn-alert removecardbtn" id="remove${ i }btn" onclick="deletecard(${ i })">
                    <i class="fa fa-trash px-1" aria-hidden="true"></i>
                </button>
            </div>
        </div>
    </div>
        <div class="col-12 mb-5">
            <div class="row">
                <div class="col-12 col-md-6 col-lg-5 my-4">
                    <div id="card${ i+1 }side1label" class="form-text">Oldal 1</div>
                    <div class="input-group d-flex">
                        <div class="input-group-text">
                            <input type="radio" name="card${ i }side1type" id="card${ i }side1typetext" value="text" class="btn" checked></input>
                            <i class="fa fa-font px-1" aria-hidden="true"></i>
                        </div>
                        <div class="input-group-text">
                            <input type="radio" name="card${ i }side1type" id="card${ i }side1typeimg" value="img" class="btn"></input>
                            <i class="fa fa-image px-1" aria-hidden="true"></i>
                        </div>
                        <input type="text" class="form-control" aria-label="text" aria-describedby="text" id="card${ i }side1text" name="card${ i }side1text" required/>
                    </div>
                </div>
                <div class="col-12 col-md-6 col-lg-5 my-4">
                    <div id="card${ i+1 }side2label" class="form-text">Oldal 2</div>
                    <div class="input-group d-flex">
                        <div class="input-group-text">
                            <input type="radio" name="card${ i }side2type" id="card${ i }side2typetext" value="text" class="btn" checked></input>
                            <i class="fa fa-font px-1" aria-hidden="true"></i>
                        </div>
                        <div class="input-group-text">
                            <input type="radio" name="card${ i }side2type" id="card${ i }side2typeimg" value="img" class="btn"></input>
                            <i class="fa fa-image px-1" aria-hidden="true"></i>
                        </div>
                        <input type="text" class="form-control" aria-label="text" aria-describedby="text" id="card${ i }side2text" name="card${ i }side2text" required/>
                    </div>
                </div>
            </div>
        </div>
    `;

    // Add card to cardlist
    cardlist.appendChild(card);

}, false);

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

        // Unbind beforeunload event
        $(window).unbind('beforeunload');

        // Copy the cardnumber value to the hidden input
        const cardnumber = document.getElementById('cardnumber');
        const seqcountinput = document.getElementById('seqcountinput');
        seqcountinput.value = cardnumber.innerHTML;

        // To-Do LOG USER IN
        form.submit()
    }
})()

// Hide delete button on the first card
const remove0btn = document.getElementById('remove0btn');
remove0btn.style.display = 'none';

// Remove card
deletecard = (id) => {
    // Get current card number
    const i = parseInt(cardnumber.innerHTML)-1;

    // Remove card
    const card = document.getElementById(`flashcard${ id }`);
    card.remove();

    // Update card number
    cardnumber.innerHTML = parseInt(cardnumber.innerHTML) - 1;

    // Renumber cards
    cardsdiv = document.getElementById('cardslist');

    for (let j = 0; j < cardsdiv.children.length; j++) {
        const card = cardsdiv.children[j];
        card.id = `flashcard${ j }`;
        card.children[0].children[0].children[0].children[0].innerHTML = `${ j+1 }. kártya`;
        card.children[0].children[0].children[1].children[0].id = `remove${ j }btn`;
        card.children[1].children[0].children[0].children[1].children[0].children[0].id = `card${ j }side1typetext`;
        card.children[1].children[0].children[0].children[1].children[1].children[0].id = `card${ j }side1typeimg`;
        card.children[1].children[0].children[0].children[1].children[2].id = `card${ j }side1text`;
        card.children[1].children[0].children[1].children[1].children[0].children[0].id = `card${ j }side2typetext`;
        card.children[1].children[0].children[1].children[1].children[1].children[0].id = `card${ j }side2typeimg`;
        card.children[1].children[0].children[1].children[1].children[2].id = `card${ j }side2text`;
    }
}

$(window).bind('beforeunload', function(){
    return 'Are you sure you want to leave?';
});