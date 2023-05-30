// Get current card
var currentCard = 0;
var queryString = window.location.href.split('?')[1];

// If query string exists, split it and retrieve the value
if (queryString) {
    var cardParam = queryString.split('=')[1];
    if (cardParam) {
        currentCard = parseInt(cardParam);
    } 
} else {
    // Set URL to current card
    window.history.pushState('', '', '?currentcard=' + currentCard);
}

var currentCardInt = currentCard
var maxCard = document.getElementById('maxcardtext');
var maxCardInt = parseInt(maxCard.innerHTML);

// If current card is greater than max card, set to max card
if (currentCardInt >= maxCardInt) {
    currentCard = '#card-' + (maxCardInt - 1);

    // Set URL to current card
    window.history.pushState('', '', '?currentcard=' + (maxCardInt - 1));

    currentCardInt = parseInt(currentCard.replace('#card-', ''));
}

// If current card is less than 0, set to 0
if (currentCardInt < 0) {
    currentCard = '#card-0';
    
    // Set URL to current card
    window.history.pushState('', '', '?currentcard=0');

    currentCardInt = parseInt(currentCard.replace('#card-', ''));
}

// Set current card
if (currentCardInt > 0) {
    document.getElementById('currentcardtext').innerHTML = currentCardInt+1;
}

// Hide all cards
for (var i = 0; i < maxCardInt; i++) {
    document.getElementById('card-' + i).classList.remove('show');
    document.getElementById('card-' + i).classList.remove('active');
    document.getElementById('card-' + i).classList.remove('d-flex');
}

// Show current card
document.getElementById('card-' + currentCardInt).classList.add('show');
document.getElementById('card-' + currentCardInt).classList.add('active');
document.getElementById('card-' + currentCardInt).classList.add('d-flex');


// prevCard function

prevCard = function() {
    var currentCard = document.getElementById('currentcardtext');
    var currentCardInt = parseInt(currentCard.innerHTML);

    if (currentCardInt > 1) {
        // Set currentCard
        currentCardInt -= 2;
        currentCard.innerHTML = currentCardInt+1;

        // Set URL to current card
        window.history.pushState('', '', '?currentcard=' + (currentCardInt));

        currentCardInt += 1;

        // Hide current card
        document.getElementById('card-' + currentCardInt).classList.remove('show');
        document.getElementById('card-' + currentCardInt).classList.remove('active');
        document.getElementById('card-' + currentCardInt).classList.remove('d-flex');

        currentCardInt -= 1;

        // Show next card
        document.getElementById('card-' + currentCardInt).classList.add('show');
        document.getElementById('card-' + currentCardInt).classList.add('active');
        document.getElementById('card-' + currentCardInt).classList.add('d-flex');
    }
}

// nextCard function

nextCard = function() {
    var currentCard = document.getElementById('currentcardtext');
    var currentCardInt = parseInt(currentCard.innerHTML);

    var maxCard = document.getElementById('maxcardtext');
    var maxCardInt = parseInt(maxCard.innerHTML);

    if (currentCardInt < maxCardInt) {
        // Set currentCard
        currentCard.innerHTML = currentCardInt+1;

        // Set URL to current card
        window.history.pushState('', '', '?currentcard=' + (currentCardInt));

        currentCardInt -= 1;

        // Hide current card
        document.getElementById('card-' + currentCardInt).classList.remove('show');
        document.getElementById('card-' + currentCardInt).classList.remove('active');
        document.getElementById('card-' + currentCardInt).classList.remove('d-flex');

        currentCardInt += 1;

        // Show next card
        document.getElementById('card-' + currentCardInt).classList.add('show');
        document.getElementById('card-' + currentCardInt).classList.add('active');
        document.getElementById('card-' + currentCardInt).classList.add('d-flex');
    }
}

// Flip card function
flipCard = function() {
    var currentCard = document.getElementById('currentcardtext');
    var currentCardInt = parseInt(currentCard.innerHTML);
    var currentCardInt = currentCardInt - 1;

    // d-none to hidden

    // If front card, flip to back
    if (document.getElementById('card' + currentCardInt + 'front').classList.contains('d-none')) {
        // Show front card
        document.getElementById('card' + currentCardInt + 'front').classList.remove('d-none');
        // Hide back card
        document.getElementById('card' + currentCardInt + 'back').classList.add('d-none');
    } else {
        // Show back card
        document.getElementById('card' + currentCardInt + 'back').classList.remove('d-none');
        // Hide front card
        document.getElementById('card' + currentCardInt + 'front').classList.add('d-none');
    }
}

// Add event listener to left arrow button to go to previous card
window.addEventListener('keydown', function(e) {
    if(e.keyCode == 32 && e.target == document.body) {
      e.preventDefault();
        flipCard();
    } else if (e.keyCode == 37 || e.keyCode == 65 && e.target == document.body) {
        e.preventDefault();
        prevCard();
    } else if (e.keyCode == 39 || e.keyCode == 68 && e.target == document.body) {
        e.preventDefault();
        nextCard();
    }
  });