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

// Set current card
if (currentCardInt > 0) {
    document.getElementById('currentcardtext').innerHTML = currentCardInt+1;
}

// Hide all cards
for (var i = 0; i < maxCardInt; i++) {
    document.getElementById('card-' + i).classList.remove('show');
    document.getElementById('card-' + i).classList.remove('active');
}

// Show current card
document.getElementById('card-' + currentCardInt).classList.add('show');
document.getElementById('card-' + currentCardInt).classList.add('active');


// prevCard function

prevCard = function() {
    var currentCard = document.getElementById('currentcardtext');
    var currentCardInt = parseInt(currentCard.innerHTML);

    var maxCard = document.getElementById('maxcardtext');
    var maxCardInt = parseInt(maxCard.innerHTML);

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

        currentCardInt -= 1;

        // Show next card
        document.getElementById('card-' + currentCardInt).classList.add('show');
        document.getElementById('card-' + currentCardInt).classList.add('active');
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

        currentCardInt += 1;

        // Show next card
        document.getElementById('card-' + currentCardInt).classList.add('show');
        document.getElementById('card-' + currentCardInt).classList.add('active');
    }
}