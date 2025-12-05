import {useState} from 'react'
let Counter=()=>{
    let[counter,setCounter]=useState(1);

    return <div>
        <h4>Counter example:</h4>
        <h4>{counter}</h4>
    <button onClick={()=>{setCounter(counter+1)}}>INCR</button>
    <button onClick={()=>{setCounter(counter-1)}}>DECR</button>
    </div>
}
export default Counter;