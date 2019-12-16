var page = 0;
showTab(page);

function showTab(n) {
  var pagesAll = document.getElementsByClassName("tab");
  pagesAll[n].style.display = "block";
  
  if (n === 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }

  if (n === pagesAll.length - 1) {
    document.getElementById("nextBtn").style.display = "none";
    document.getElementById("enviar").style.display = "inline";
    //document.getElementById("nextBtn").setAttribute('type', 'submit');
  } else {
    document.getElementById("nextBtn").innerHTML = "Próximo";
    document.getElementById("enviar").style.display = "none";
  }
}

const btnAnterior = document.getElementById("prevBtn");
btnAnterior.addEventListener("click", function() {
  document.getElementById("nextBtn").style.display = "inline";
  document.getElementById("enviar").style.display = "none";
});

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");

  //if (n == 1 && !validateForm()) return false;

  // Hide the current tab:
  x[page].style.display = "none";
  // Increase or decrease the current tab by 1:
  page = page + n;
  // Otherwise, display the correct tab:
  showTab(page);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x,
    y,
    i,
    valid = true;
  x = document.getElementsByClassName("tab");
  y = x[page].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false
      valid = false;
    }
  }
  return valid; // return the valid status
}

/*****************  Select of Citys  ******************* */

// Chamando função para Select de Estado e Cidade

new dgCidadesEstados({
  cidade: document.getElementById("cidade"),
  estado: document.getElementById("estado")
});

