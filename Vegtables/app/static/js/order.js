// function addRow() {
//   const table = document.getElementById('vegTable').getElementsByTagName('tbody')[0];
//   const row = table.insertRow();
//   row.innerHTML = `
//     <td><input name="veg_name[]" class="form-control" required></td>
//     <td><input name="veg_price[]" type="number" step="0.01" class="form-control" oninput="updateRow(this)" required></td>
//     <td><input name="veg_kg[]" type="number" step="0.01" class="form-control" oninput="updateRow(this)" required></td>
//     <td><input name="amount[]" readonly class="form-control"></td>
//     <td><button type="button" class="btn btn-danger" onclick="removeRow(this)">Remove</button></td>
//   `;
// }

// function removeRow(button) {
//   button.closest('tr').remove();
//   updateTotal();
// }

// function updateRow(input) {
//   const row = input.closest('tr');
//   const price = parseFloat(row.querySelector('[name="veg_price[]"]').value) || 0;
//   const kg = parseFloat(row.querySelector('[name="veg_kg[]"]').value) || 0;
//   const amount = price * kg;
//   row.querySelector('[name="amount[]"]').value = amount.toFixed(2);
//   updateTotal();
// }

// function updateTotal() {
//   let total = 0;
//   document.querySelectorAll('[name="amount[]"]').forEach(input => {
//     total += parseFloat(input.value) || 0;
//   });
//   document.getElementById('totalAmount').innerText = 'Total Amount: ₹' + total.toFixed(2);
// }

// window.onload = () => addRow();

let rowCount = 0;

function addRow() {
    const table = document.querySelector("#order-table tbody");
    const row = document.createElement("tr");
    row.innerHTML = `
        <td><input type="text" class="form-control veg_name"></td>
        <td><input type="number" class="form-control veg_price" oninput="updateAmount(this)"></td>
        <td><input type="number" class="form-control veg_kg" oninput="updateAmount(this)"></td>
        <td><input type="text" class="form-control amount" readonly></td>
        <td><button type="button" class="btn btn-danger btn-sm" onclick="removeRow(this)">x</button></td>
    `;
    table.appendChild(row);
}

function updateAmount(el) {
    const row = el.closest('tr');
    const price = parseFloat(row.querySelector('.veg_price').value) || 0;
    const kg = parseFloat(row.querySelector('.veg_kg').value) || 0;
    const amount = price * kg;
    row.querySelector('.amount').value = amount.toFixed(2);
    updateTotal();
}

function updateTotal() {
    let total = 0;
    document.querySelectorAll('.amount').forEach(input => {
        total += parseFloat(input.value) || 0;
    });
    document.querySelector('#total-amount').value = total.toFixed(2);
}

function removeRow(btn) {
    btn.closest('tr').remove();
    updateTotal();
}

document.querySelector("#order-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const items = [];
    document.querySelectorAll("#order-table tbody tr").forEach(row => {
        const veg_name = row.querySelector(".veg_name").value;
        const veg_price = parseFloat(row.querySelector(".veg_price").value) || 0;
        const veg_kg = parseFloat(row.querySelector(".veg_kg").value) || 0;
        const amount = parseFloat(row.querySelector(".amount").value) || 0;

        if (veg_name && veg_price && veg_kg) {
            items.push({ veg_name, veg_price, veg_kg, amount });
        }
    });

    const total_amount = parseFloat(document.querySelector("#total-amount").value) || 0;

    fetch("/api/save_order/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({ items, total_amount }),
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === 'success') {
            alert("Order submitted! Order ID: " + data.order_id);
            location.reload();
        } else {
            alert("Error saving order.");
        }
    });
});

// Helper to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const trimmed = cookie.trim();
            if (trimmed.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(trimmed.slice(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

