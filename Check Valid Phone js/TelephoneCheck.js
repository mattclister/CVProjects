function telephoneCheck(str) {

// List of valid formats
let validFormats = [
  "555-555-5555",
  "(555)555-5555",
  "(555) 555-5555",
  "555 555 5555",
  "5555555555",
  "1 555 555 5555",
  "1 555-555-5555",
  "1 (555) 555-5555",
  "1(555)555-5555"
]

// List of Numbers
let numbers = ["1","2","3","4","5","6","7","8","9","0"]

// Split the string into array
let splitStr = str.split("")

// Remove non numbers
let numberStr = splitStr.filter((item) => {if(numbers.indexOf(item) != -1) {return true}})

// Get count of numbers
let numberStrLength = numberStr.length

// Country code check
if (numberStrLength == 11 & numberStr[0] != "1") {return false}

// Convert all numbers to 5
let strFormatted = str.replaceAll(/[\d]/g,"5")
if (numberStrLength == 11) {
  let strFormattedArray = strFormatted.split("")
  strFormattedArray[0] = "1"
  strFormatted = strFormattedArray.join("")
  console.log(`Str = ${str} Replacement = ${strFormatted}`)
}

// Check Format
if (validFormats.indexOf(strFormatted)!=-1) {return true}
else {return false}

}

telephoneCheck("1(555)555-5555");
