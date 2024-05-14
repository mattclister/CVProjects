function convertToRoman(num) {

    let numbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    
    let letters = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    
    let numberArray = []
    
    function splitNumber(num) {
    if (num === 0) {
      return numberArray
    } else {
        for (let i = 0; i<numbers.length; i++) {
        if (num >= numbers[i]) {
          numberArray.push(numbers[i])
          num = num - numbers[i]
          return splitNumber(num)
        }
      }
    }
    }
    
    let numArray = splitNumber(num)
    let letterArray = []
    
    for (let i = 0; i < numArray.length; i++) {
      letterArray.push(letters[numbers.indexOf(numArray[i])])
    }
    
    letterArray = letterArray.join("")
    console.log(letterArray)
    
    return letterArray
    
    }
