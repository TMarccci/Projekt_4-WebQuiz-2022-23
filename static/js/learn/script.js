// Set the current card from URL
var currentCard = window.location.hash;
// If no current card, set to 0
if (currentCard == '') {
    currentCard = '#card-0';
    // Set URL to current card
    window.location.href = currentCard;
}

var currentCardInt = parseInt(currentCard.replace('#card-', ''));
var maxCard = document.getElementById('maxcardtext');
var maxCardInt = parseInt(maxCard.innerHTML);

// If current card is greater than max card, set to max card
if (currentCardInt >= maxCardInt) {
    currentCard = '#card-' + (maxCardInt - 1);
    // Set URL to current card
    window.location.href = currentCard;
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

        // Redirect to last card with id of maxCard
        window.location.href = '#card-' + currentCardInt;

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

        // Redirect to last card with id of maxCard
        window.location.href = '#card-' + currentCardInt;

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