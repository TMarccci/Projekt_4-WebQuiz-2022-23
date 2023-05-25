function removeOptions(objSelect) {
  while (objSelect.options.length > 0) objSelect.options[0] = null;
}

function run() {
  // Get the value from text box
  var textcontent = document.getElementById("searchtext");
  // Get wich category is selected with the radio button
  var category = document.querySelector('input[name="categoryfilter"]:checked');

  var values = {
    searchtext: textcontent.value,
    categoryfilter: category.value,
  };

  // AJAX > to check //
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/searchapi", true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

  xhr.onreadystatechange = function () {
    if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
      console.log(this.responseText);
      var objects = JSON.parse(this.responseText);

      var cardholder = document.getElementById("cardholder");

      // Remove all cards
      while (cardholder.firstChild) {
        cardholder.removeChild(cardholder.firstChild);
      }

      for (var quiz in objects) {
        var cardcol = document.createElement("div");
        cardcol.className = "col-12 col-md-6 col-lg-4 my-3";

        var card = document.createElement("div");
        card.className = "card";

        var cardbody = document.createElement("div");
        cardbody.className = "card-body";

        var cardcontroller = document.createElement("span");
        cardcontroller.className = "px-2 py-1 float-end ms-2 cardscontroller";
        cardcontroller.innerHTML = objects[quiz][7];

        var cardlink = document.createElement("a");
        cardlink.href = "/quiz/" + objects[quiz][1];
        cardlink.innerHTML = objects[quiz][2];

        var cardcategory = document.createElement("p");
        cardcategory.innerHTML = objects[quiz][3];

        cardcol.appendChild(card);
        card.appendChild(cardbody);
        cardbody.appendChild(cardcontroller);
        cardbody.appendChild(cardlink);
        cardbody.appendChild(cardcategory);

        cardholder.appendChild(cardcol);
      }
    }
  };

  var params = "_=" + Math.floor(Date.now() / 1000);
  for (var key in values) {
    params += "&" + key + "=" + values[key];
  }
  xhr.send(params);
}

var submit = document.getElementById("submitsearch");
if (submit != null) {
  submit.addEventListener("click", run);
}

run();

if (document.querySelector('input[name="categoryfilter"]')) {
  document.querySelectorAll('input[name="categoryfilter"]').forEach((elem) => {
    elem.addEventListener("change", function(event) {
      run();
    });
  });
}


