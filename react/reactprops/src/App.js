// import CompA from './props/CompA'
// // import CompB from './props/CompB'
// // import Movie from './props/Movie'
// import User from './props2/User'
// let App=()=>{
//     return <div>app component
//         <User/>
//         <CompA/>
//     </div>

// }
// export default App;

// import React  from 'react'
// import CompA from './props/CompA'
// import CA from './props/PD/CA'
// let App=()=>{
//     return <React.Fragment>
//         <h2>App component</h2>
//         <CompA/>
//         <CA/>
//     </React.Fragment>
// }
// export default App;
import CompB from "./props/CompB";
let App=()=>{
    const eid=101;
    const ename="madhu";
let greet=()=>{
    return "good morning"
}
let employees=[{"eid":1,"ename":"Had","gender":"Male"},
        {"eid":2,"ename":"Lyn","gender":"Male"},
        {"eid":3,"ename":"Bert","gender":"Male"},
        {"eid":4,"ename":"Hiram","gender":"Non-binary"},
        {"eid":5,"ename":"Gui","gender":"Female"},
        {"eid":6,"ename":"Raeann","gender":"Agender"},
        {"eid":7,"ename":"Sybila","gender":"Female"},
        {"eid":8,"ename":"Carmon","gender":"Female"},
        {"eid":9,"ename":"Any","gender":"Male"},
        {"eid":10,"ename":"Giana","gender":"Female"}];
    return <div>
        <h2>app component</h2>
        <h2>eid:{eid}</h2>
        <h2>ename:{ename}</h2>
        <h2>total:{100*20}</h2>
        <h2>{greet()}</h2>
        <CompB employees={employees}/>

    </div>

}
export default App;