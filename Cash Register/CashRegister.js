function checkCashRegister(price, cash, cid) {


// Change due is calculated
let change = cash - price

console.log(
"--------------------------------NEW ENTRY----------------------------------")
console.log(`PRICE: ${price} CASH: ${cash} CHANGE: ${change}
CID: ${cid}
----------------------------------------------------------------------------`)
  
// Dictionary of coin values
let coinNameValues = {
      "PENNY": 0.01,
      "NICKEL": 0.05,
      "DIME": 0.1,
      "QUARTER": 0.25,
      "ONE": 1,
      "FIVE": 5,
      "TEN": 10,
      "TWENTY": 20,
      "ONE HUNDRED": 100
    };

let cashOut = {}

// Function to create drawers
function CreateDrawer(coinName,amount) {
  this.name = coinName;
  this.value = coinNameValues[coinName];
  this.amount = amount;
  this.units = Math.round(this.amount / this.value);
  this.active = true
};

// Function to remove a unit
function CashOut(coinName) {
  console.log(`start: COIN ${coinName} VALUE: ${cashdrawer[coinName]["value"]} CHANGE: ${change}`)
  cashdrawer[coinName]["amount"] = Math.round(cashdrawer[coinName]["amount"]*100 - cashdrawer[coinName]["value"]*100)/100;
  cashdrawer[coinName]["units"] -= 1;
  change = Math.round(change*100 - cashdrawer[coinName]["value"]*100)/100
  if (cashOut.hasOwnProperty(coinName)) {cashOut[coinName] = Math.round(cashOut[coinName]*100 + cashdrawer[coinName]["value"]*100)/100}
  else {cashOut[coinName] = cashdrawer[coinName]["value"]}
  console.log(`end: COIN ${coinName} VALUE: ${cashdrawer[coinName]["value"]} CHANGE: ${change}`)
}

// Function to check if coin active
function CheckActive(coinName) {
  if (cashdrawer[coinName]["value"] <= change & cashdrawer[coinName]["units"] >= 1) {
    return true
  } else {return false}
}

// Create drawers
let cashdrawer = {};
for (let i = 0 ; i < cid.length ; i++) {
  let coinName = cid[i][0];
  let coinAmount = cid[i][1];
  cashdrawer[coinName] = (new CreateDrawer(coinName,coinAmount))
  }

// Calculate change

for (let i = Object.keys(coinNameValues).length -1; i >= 0; i--){
  let prop = Object.keys(coinNameValues)[i]
  cashdrawer[prop]["active"] = CheckActive(prop)
  console.log(`Checking coin: ${cashdrawer[prop]["name"]}, ${cashdrawer[prop]["active"]}`)
    while (cashdrawer[prop]["active"] == true) {
      CashOut(cashdrawer[prop]["name"])
      cashdrawer[prop]["active"] = CheckActive(prop)
    }
  }

// Calculate Total Amount

let totalAmount = 0;
for (let i = 0; i<Object.entries(cashdrawer).length;i++) {
  totalAmount = totalAmount + Math.round(Object.entries(cashdrawer)[i][1]["amount"])
}

// Create Output

      let output = {status: "OPEN", change: Object.entries(cashOut)}

      // Check funds sufficient
      if (change > 0) {
        output.status = "INSUFFICIENT_FUNDS";
        output.change = []
      }

      // Check if till is empty
      console.log(`Total amount = ${totalAmount}`)
      console.log(`Change = ${change}`)

      if (totalAmount == 0 & change == 0) {
        output.status = "CLOSED";
        output.change = cid
      }

      // Return Output

      console.log(output)
      return output

}
  
  checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
