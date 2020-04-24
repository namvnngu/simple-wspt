// Global variables
let jobID = document.getElementById("job");
let pElement = document.getElementById("p-value");
let wElement = document.getElementById("w-value");
let submitButton = document.getElementById("submit-button");
let calButton = document.getElementById("cal-button");
let sortingButton = document.getElementById("sorting-button");
let renewButton = document.getElementById("renew-button");
let bodyTable = document.querySelector("table tbody");
let minWC = document.getElementById("result");
let table = [];

// Row Addition
function addRow() {
  let id = jobID.value;
  let p = pElement.value;
  let w = wElement.value;
  let row = [id, parseFloat(p), parseFloat(w), parseFloat(w) / parseFloat(p)];
  table.push(row);

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
  sortingButton.disabled = false;
  let row = document.createElement("tr");
  let arr = [id, p, w];
  let cell;
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
function sorting() {
  calButton.disabled = false;
  if (table != []) {
    table.sort(function (a, b) {
      if (a[3] == (0)[3]) {
        return 0;
      } else {
        return a[3] < b[3] ? 1 : -1;
      }
    });
  }
  bodyTable.textContent = "";
  table.map(function (row) {
    createRow(row[0], row[1], row[2]);
  });
}

// Min calculation
function calculateMin() {
  let result = 0;
  let c = 0,
    w = 0;
  for (let i = 0; i < table.length; i++) {
    c += table[i][1];
    w = table[i][2];
    result += c * w;
  }
  minWC.innerHTML = result;
}

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
sortingButton.addEventListener("click", sorting);
calButton.addEventListener("click", calculateMin);
renewButton.addEventListener("click", function () {
  table = [];
  bodyTable.textContent = "";
  sortingButton.disabled = true;
  calButton.disabled = true;
  minWC.innerHTML = "0";
});
