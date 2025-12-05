import React,{useState} from 'react'
let Message=()=>{
    // let msg="hello"
    let[msg,setMsg]=useState("hello....")
    // let gmHandler=()=>{
    //     setMsg("Good Morning")
    // }
    // let gnHandler=()=>{
    //     setMsg("Good Night")
    // }
    // let gaHandler=()=>{
    //     setMsg("Good Afternoon")
    // }
       let updateHandler=(msg)=>{
            setMsg(msg)
        }
    return <div>
        <h2>Message comp</h2>
        <h2>Message:{msg}</h2>
        {/* <button onClick={gmHandler}>GM</button>
        <button onClick={gnHandler}>GN</button>
        <button onClick={gaHandler}>GA</button> 
        <button onClick={()=>{setMsg("Good Evening")}}>GE</button> */}
        <button onClick={updateHandler.bind(null,"GM")}>GM</button>
        <button onClick={updateHandler.bind(null,"GA")}>GA</button>
        <button onClick={updateHandler.bind(null,"GN")}>GN</button>
    </div>

}
export default Message;