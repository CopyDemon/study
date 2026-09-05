// basic print
print("Hello Wrold")

// constant values
// let a = 1 the value can't be reassign later
// var a = 1 the value can be reassign but reassign value has to be same type with initial value type
// assign basic value and print
var constValue = "constant"
print("constant variable value is:")
print(constValue)

// update existing variable and print
print("update constant value from 'constant' to '77'.")
constValue = "77"
print("up to date constant value is:")
print(constValue)

/*
    Notice once the variable assigned one type of value it may not be assign another type
*/

// define a variable type
var name : String = "Sheng"
print("Name is: " + name)

// Experiment
var myFloat : Float = 4
print(myFloat)

// different type value operation
let label = "The width is "
let width = 94
let widthLabel = label + String(width) // here make new variable to store new value
print(widthLabel)
