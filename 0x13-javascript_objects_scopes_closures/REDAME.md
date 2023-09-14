JavaScript Objects:
In JavaScript, an object is a complex data type that allows you to store a collection of key-value pairs, where the keys are strings (or Symbols) and the values can be of any data type, including other objects. Objects are the building blocks of JavaScript, and they are used extensively in the language.
Here's how you can create an object in JavaScript using object literal notation:
const person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
};
You can access the properties of an object using dot notation (e.g., person.firstName) or bracket notation (e.g., person['firstName']).

Scope:
Scope refers to the context in which variables and functions are declared and can be accessed in JavaScript. JavaScript has two main types of scope:

Global Scope: Variables declared in the global scope are accessible from anywhere in your code. They are declared outside of any function or block.
const globalVar = 10;

function someFunction() {
    console.log(globalVar); // Accessible
}
Local Scope (Function Scope): Variables declared inside a function are only accessible within that function. They have local scope.
function someFunction() {
    const localVar = 20;
    console.log(localVar); // Accessible
}
console.log(localVar); // Not accessible (generates an error)
In modern JavaScript (ES6+), you can also use let and const to create block-scoped variables, which are only accessible within the block they are defined in.
if (true) {
    const blockVar = 30;
}
console.log(blockVar); // Not accessible (generates an error)

Closures:
A closure is a JavaScript feature that occurs when a function remembers
