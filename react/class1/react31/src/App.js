// // import Message from './state/Message'
// // import Counter from './state/Counter'
// // import Counter2 from './state/Counter2'
// // let App=()=>{
// //     return <div>
// //         <h2>App component</h2>
// //         <Message/>
// //         {/* <Counter/>
// //         <Counter2/> */}
// //     </div>
// // }
// // export default App;
// // import Messages from "./state/class-styling/Messages";
// // import '../node_modules/bootstrap/dist/css/bootstrap.css'
// // import Navbar from './state/class-styling/Navbar/Navbar'
// // let App=()=>{
// //     return <div>
// //           <Navbar/>
// //         <Messages/>
// //     </div>
// // }
// // export default App;
// import Message from './state/Message'
// let App=()=>{
//     return <div>
//         <h2>App component</h2>
//         <Message/>
//     </div>
// }
// export default App;

// import User from './Restapi-axios/User'
// import Users from './Restapi-axios/Users'


// import Albums from './Restapi-axios/Albums'

// let App=()=>{
//     return <div>
//         {/* <User/>
//         <Users/> */}
//         <Albums/>
//     </div>
// }
// export default App;




import Navbar from "./routing/Navbar";
import {BrowserRouter as Router,Routes,Route} from 'react-router-dom'
import Home from './routing/header/Home'
import Contact from './routing/header/Contact'
import Login from './routing/header/Login'
// import Navbar1 from "./routing/Navbar1"
let App=()=>{
    return <div>
        <Router future={{
                    v7_startTransition: true,
                    v7_relativeSplatPath: true,}}>
            <Navbar/>
            <Routes>
                <Route path="/"  element={<Home/>}/>
                <Route path="/home"  element={<Home/>}/>
                <Route path="/contact"  element={<Contact/>}/>
                <Route path="/login"  element={<Login/>}/>
            </Routes>
        </Router>
    </div>
}
export default App;








