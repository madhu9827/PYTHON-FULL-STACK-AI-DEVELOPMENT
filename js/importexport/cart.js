//default import
// let pname = require('./product'); // ✅ works in CommonJS
// console.log(pname);
// import product from './product.js'
// new product();
import { pname, Product } from './one.js';

new Product();
console.log(pname);
