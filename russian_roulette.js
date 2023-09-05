// firePosition ist die Position, in der die Waffe abgefeuert wird.
let firePosition = 1;

// Die Ausgabe von spinChamber ist eine "zufällige" Zahl und kann als Parameter an die Funktion fireGun übergeben werden.
const spinChamber = () => {
  return Math.floor(Math.random() * 6) + 1; // Erzeugt eine zufällige Zahl zwischen 1 und 6
};

// fireGun prüft, ob die Zahl aus spinChamber mit der Zahl aus firePosition übereinstimmt.
// Falls JA, wird "Du bist 🔫" zurückgegeben, falls NEIN, wird "Spiel weiter 🎲" zurückgegeben.
const fireGun = (bulletPosition) => {
  if (bulletPosition === firePosition) {
    return "Du bist 🔫";
  } else {
    return "Spiel weiter 🎲";
  }
};

console.log(fireGun(spinChamber()));
