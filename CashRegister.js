function checkCashRegister(price, cash, cid) {
  console.log("--------------NEW ENTRY--------------------")
  console.log(`PRICE: ${price} CASH: ${cash}
  CID: ${cid}`)
  // Change due is calculated
    let change = cash - price
  
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
    }
  
  // Function creating an object for each "Drawer of coins" in the cash register
    function drawer(name,amount) {
      let value = coinNameValues[name]
      this.name = name;
      this.amount = amount;
      this.value = value
      this.units = Math.round(amount/value);
    }
  
  // Create a drawer for each corresponding drawer in CID, add to drawers
  let drawers = []
  for (let i = 0; i < cid.length; i++) {
     drawers.push(new drawer(cid[i][0],cid[i][1]))
  }
  
  // Resolve what change to give with recursive function
  let coinArray = {}
  
  function changeCalc(change) {
    console.log(`-------------------
  Change: ${change}`)
    if (change <= 0) {return coinArray} else {
      for (let i = drawers.length-1;i>=0;i--) {
        if (change >= drawers[i]["value"] & drawers[i]["units"] > 1) {
            console.log(`Change Taken: ${drawers[i]["value"]}`)
            drawers[i]["units"] = drawers[i]["units"] - 1
            drawers[i]["amount"] = drawers[i]["amount"] - drawers[i]["value"]
            change = Math.round(change - drawers[i]["value"])
            coinArray[drawers[i]["name"]] = drawers[i]["value"]])
            console.log(drawers)
            return changeCalc(change)
        }
      }
    }
  }
  changeCalc(change)
  
  // Summarise Coins
  
  console.log(coinArray)
  
  // Sum by coin
  
  }
  
  checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);