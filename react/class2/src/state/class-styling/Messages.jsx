import './Message.css'

let Messages=()=>{
    let myStyle={color:"pink"};
    return <div>
        <h2 style={{color:"blue"}}>GM</h2>
        <h2 style={myStyle}>GA</h2>
        <h2 className="box">GE</h2>
        <button className='btn btn-danger'>TEST</button>
    </div>
}
export default Messages;