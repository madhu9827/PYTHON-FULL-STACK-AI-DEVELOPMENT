import Axios from 'axios'
import {useState} from 'react'
let User=()=>{
    let[users,setUser]=useState([])
    let getuseHandler=()=>{
        console.log("test case 123")
        Axios.get('https://jsonplaceholder.typicode.com/users')
        .then((resp)=>{setUser(resp.data)})
        .catch((err)=>{console.log(err.name)})
    }

        return <div>
            {/* <h2>User component</h2>*/}
            <button onClick={getuseHandler}>get details</button> 
            <pre>{JSON.stringify(users)}</pre>
            <table border="2">
                <thead>
                    <tr>
                    <th>user id</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>city</th>
                    </tr>
                 
                </thead>
                <tbody>
                    {
                        users.map((user,Index)=>{
                            return <tr key={Index}>
                                    <td>{user.id}</td>
                                    <td>{user.name}</td>
                                    <td>{user.email}</td>
                                    <td>{user.address.city}</td>
                            </tr>
                        })
                    }
                </tbody>
            </table>

        </div>
}
export default User;