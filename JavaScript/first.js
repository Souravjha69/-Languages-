let fullname = "Sourav kumar jha";
console.log (fullname) ; 

// Javascript is dynamically typed language here : 
age = 24;  // {=} Equal to means here Assignment oprator means 24 age ke andr jake store ho gyi hai . 
price = 99.9;
console.log (age);
console.log (price);

x = null; // Iska mtlb x ke andr value to hai , but khali hai ye :
console.log (x);
y = undefined; // Iska mtlb , value y me pata hi nahi hai :
console.log (y);

isFollow = true; // In this we store only two types of value true or false , only these values.
console.log (isFollow);
isFollow2 = false; // We store only two types of Values here.
console.log (isFollow2);
Console = 25; // Here console is a reserved keyword :
console.log (Console);

// let price = 56;
// console.log (typeof(price));

// let price = 56; // Declares a variable 'price' and assigns it the value 56
// console.log(typeof(price));

const student = { // This is Objects here : 
    fullName : "Sourav kumar jha",
    age : 20,
    cgpa : 8.0,
    isPass : true,
}
console.log(student);
console.log (student["fullName"]); // printing key value pairs :
console.log (student.age);

// ................................//
//......Practice Question Q.1......//

const Product = {
    fullName : "Parker Jotter Standard CT Ball Pen",
    color : "Black",
    rating : 7002,
    price : 270,
    isDeal : true,
    offerPercentage : 5,
}
console.log (Product);
console.log (Product.rating);
console.log(Product.fullName);
console.log(Product["offerPercentage"]);
console.log (Product.isDeal);
Product.isDeal = false;
console.log (Product.isDeal);// I'm updated the value just for practice here :
