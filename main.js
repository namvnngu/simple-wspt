// Global variables
let jobID = document.getElementById("job");
let pElement = document.getElementById("p-value");
let wElement = document.getElementById("w-value");
let submitButton = document.getElementById("submit-button");
let table = [];

// Row Addition
function addRow() {
  let id = jobID.value;
  let p = pElement.value;
  let w = wElement.value;
  let row = [id, parseFloat(p), parseFloat(w), parseFloat(w) / parseFloat(p)];
  table.push(row);
  console.log(table);

  if (id != "" && p != "" && w != "") {
    createRow(id, parseFloat(p), parseFloat(w));
  } else {
    alert("Please fill enough three text fields");
  }

  jobID.value = "";
  pElement.value = "";
  wElement.value = "";
}

function createRow(id, p, w) {
  let row = document.createElement("tr");
  let arr = [id, p, w];
  let cell;
  let bodyTable = document.querySelector("table tbody");
  row.classList.add("d-flex");

  for (let i = 0; i < 3; i++) {
    cell = document.createElement("td");
    cell.classList.add("col");
    cell.innerHTML = arr[i];
    row.appendChild(cell);
  }
  bodyTable.appendChild(row);
}

// Sorting the table

// Min calculation

// Events
window.onload = function () {
  jobID.focus();
};
submitButton.addEventListener("click", addRow);
wElement.addEventListener("keyup", function (e) {
  if (e.keyCode == 13) {
    e.preventDefault();
    submitButton.click();
    jobID.focus();
  }
});
