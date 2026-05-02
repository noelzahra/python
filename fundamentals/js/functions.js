/* Basics */
var total = function(num1, num2) {
  return num1 + num2;
};

console.log(total(11, 22));

var multiply = function(num1, num3, num4) {
  return num1 * num3 * num4;
};

console.log(multiply(10, 20, 5));

function person(firstName, secondName) {
  return firstName + ' ' + secondName;
}

var player = person('Pierre', 'Zahra');
console.log(player);

/* Constructor*/
var Customer = function(firstName, lastName, city) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.city = city;
  this.concat = function() {
    return this.firstName + ' ' + this.lastName;
  };
}

var member = new Customer('Pierre', 'Zahra');

/* Constructor with  multiple params */

var Holiday = function(info) {
  this.destination = info.destination;
  this.stay = info.days;
  this.cost = info.price;
};

var london = new Holiday({destination: 'London',
                         days: '10',
                         price: '1200'
                         });

console.log('City: ' + london.destination + '\n' + 'Stay: ' + london.stay + '\n' + 'Price: ' + london.cost);

/* Using instanceof operator */
function Transport(mode) {
  if (!(this instanceof Transport))
    return new Transport(mode);
    this.line = mode;
}
Transport('trian');
console.log(Transport('trian'));

/* Fizzbuzz*/
function fizzbuzz(max) {

  var array = [];

  function check(num) {
    string = '';
    if (num %3 === 0) { string += 'fizz'};
    if (num %5 === 0) { string += 'buzz'};
    return string || num;
  }

  for(var i =0; i <= max; i++) {
    array.push(check(i));
  }

  return array;
}
console.log( fizzbuzz(30));

function Sport(info) {
  this.name = info.name;
  this.team = info.team;
  this.city = info.city;
};

var marathon = new Sport ({
  name: 2015,
  team: 'Pro',
  city: 'London'
});

console.log('Marathon details: ' + marathon.name + '\n' + marathon.team + '\n' + marathon.city);
