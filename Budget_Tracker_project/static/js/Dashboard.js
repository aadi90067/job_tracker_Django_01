function switchs() {
  const isDark = document.body.classList.toggle("dark-mode");
  document.body.classList.toggle("light-mode", !isDark);

  // Save mode to localStorage
  localStorage.setItem("theme", isDark ? "dark" : "light");
}

// Load saved theme on page load
const savedTheme = localStorage.getItem("theme");
if (savedTheme === "dark") {
  document.body.classList.add("dark-mode");
} else {
  document.body.classList.add("light-mode");
}

let form = document.getElementById("expense-form");
let categoryList = document.getElementById("category");
let amountList = document.getElementById("amount");
let expenseList = document.getElementById("expense-list");

const expenses = {
  "Food": 0,
  "Shopping": 0,
  "EMI/Loans": 0,
  "Enjoy/Entertainment": 0,
  "Transport": 0,
  "Medical/Healthcare": 0,
  "Utilities": 0,
  "Personal Care": 0,
  "Savings/Investments": 0,
  "Gifts/Donations": 0,
  "Education": 0,
  "Household Items": 0,
  "Pets": 0,
};

function listshow() {
  expenseList.innerHTML = "";
  for (let cat in expenses) {
    const div = document.createElement("div");
    div.className = "expense-item";
    div.innerHTML = `<p>${cat} :</p><p>₹ ${expenses[cat].toFixed(2)}</p>`;
    expenseList.appendChild(div);
  }
}

// Form submit handler
form.addEventListener("submit", function (e) {
  e.preventDefault();

  let category = categoryList.value;
  let amount = parseFloat(amountList.value);

  if (!isNaN(amount) && amount > 0) {
    expenses[category] += amount;
    listshow();
    form.reset();
  }
});

// Initial display
listshow();
