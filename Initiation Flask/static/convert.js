
function Calcul() {
    let val = document.getElementById("entier").value;
    if (isNaN(val)) return alert("L'entier saisi n'est pas valide !")
    let nbDecimal = parseInt(val);
    
    if (document.getElementById("binaire").checked) {
      let nbBinaire = nbDecimal.toString(2);
      document.getElementById("resultat").value = nbBinaire;
    } else if (document.getElementById("hexa").checked) {
      let nbHexa = nbDecimal.toString(16)
      document.getElementById("resultat").value = nbHexa.toUpperCase();
    }
  
  }