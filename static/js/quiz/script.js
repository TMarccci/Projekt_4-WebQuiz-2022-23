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

if (publicquiz.checked) {
    apperainsearch.disabled = false;
}

const cardnumber = document.getElementById('cardnumber');
const addcard = document.getElementById('addcard');
const cardlist = document.getElementById('cardslist');

/*
<div class="flashcard">
    <div class="h5">{{ i+1 }}. kártya</div>
        <div class="col-12 mb-5">
            <div class="row">
                <div class="col-12 col-md-6 col-lg-5 my-4">
                    <div id="card${ i+1 }side1label" class="form-text">Oldal 1</div>
                    <div class="input-group d-flex">
                        <div class="input-group-text">
                            <input type="radio" name="card${ i+1 }side1type" id="card${ i+1 }side1typetext" class="btn" checked></input>
                            <i class="fa fa-font px-1" aria-hidden="true"></i>
                        </div>
                        <div class="input-group-text">
                            <input type="radio" name="card${ i+1 }side1type" id="card${ i+1 }side1typeimg" class="btn"></input>
                            <i class="fa fa-image px-1" aria-hidden="true"></i>
                        </div>
                        <input type="text" class="form-control" aria-label="text" aria-describedby="text" id="card${ i+1 }side1text" name="card${ i+1 }side1text" required/>
                    </div>
                </div>
                <div class="col-12 col-md-6 col-lg-5 my-4">
                    <div id="card${ i+1 }side2label" class="form-text">Oldal 2</div>
                    <div class="input-group d-flex">
                        <div class="input-group-text">
                            <input type="radio" name="card${ i+1 }side2type" id="card${ i+1 }side2typetext" class="btn" checked></input>
                            <i class="fa fa-font px-1" aria-hidden="true"></i>
                        </div>
                        <div class="input-group-text">
                            <input type="radio" name="card${ i+1 }side2type" id="card${ i+1 }side2typeimg" class="btn"></input>
                            <i class="fa fa-image px-1" aria-hidden="true"></i>
                        </div>
                        <input type="text" class="form-control" aria-label="text" aria-describedby="text" id="card${ i+1 }side2text" name="card${ i+1 }side2text" required/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
*/

addcard.addEventListener('click', () => {
    cardnumber.innerHTML = parseInt(cardnumber.innerHTML) + 1;

    // Get current card number
    const i = parseInt(cardnumber.innerHTML)-1;

    // Add card to cardlist
    const card = document.createElement('div');
    card.classList.add('flashcard');
    card.innerHTML = `
        <div class="h5">${ i+1 }. kártya</div>
        <div class="col-12 mb-5">
            <div class="row">
                <div class="col-12 col-md-6 col-lg-5 my-4">
                    <div id="card${ i+1 }side1label" class="form-text">Oldal 1</div>
                    <div class="input-group d-flex">
                        <div class="input-group-text">
                            <input type="radio" name="card${ i+1 }side1type" id="card${ i+1 }side1typetext" value="text" class="btn" checked></input>
                            <i class="fa fa-font px-1" aria-hidden="true"></i>
                        </div>
                        <div class="input-group-text">
                            <input type="radio" name="card${ i+1 }side1type" id="card${ i+1 }side1typeimg" value="img" class="btn"></input>
                            <i class="fa fa-image px-1" aria-hidden="true"></i>
                        </div>
                        <input type="text" class="form-control" aria-label="text" aria-describedby="text" id="card${ i+1 }side1text" name="card${ i+1 }side1text" required/>
                    </div>
                </div>
                <div class="col-12 col-md-6 col-lg-5 my-4">
                    <div id="card${ i+1 }side2label" class="form-text">Oldal 2</div>
                    <div class="input-group d-flex">
                        <div class="input-group-text">
                            <input type="radio" name="card${ i+1 }side2type" id="card${ i+1 }side2typetext" value="text" class="btn" checked></input>
                            <i class="fa fa-font px-1" aria-hidden="true"></i>
                        </div>
                        <div class="input-group-text">
                            <input type="radio" name="card${ i+1 }side2type" id="card${ i+1 }side2typeimg" value="img" class="btn"></input>
                            <i class="fa fa-image px-1" aria-hidden="true"></i>
                        </div>
                        <input type="text" class="form-control" aria-label="text" aria-describedby="text" id="card${ i+1 }side2text" name="card${ i+1 }side2text" required/>
                    </div>
                </div>
            </div>
        </div>
    `;

    // Add card to cardlist
    cardlist.appendChild(card);

}, false);

const submitbutton = document.getElementById('submitbutton');

submitbutton.addEventListener('click', () => {
    const form = document.getElementById('caardsform');
    form.submit();
}, false);