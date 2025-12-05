// let CompB=(x)=>{
//     return <div>
//         <h2>Component B</h2>
//         <pre>{JSON.stringify(x)}</pre>
//         <h1>eid:{x.eid}</h1>
//         <h2>ename:{x.ename}</h2>
//     </div>
// }
// export default CompB;
import React from 'react'

const CompB = (props) => {
  let { greet, emp_Id } = props; // Object Destructuring

  return (
    <div>
      <h3>Component B</h3>
      <h3>{JSON.stringify(props)}</h3>
      <h4>{greet}</h4>
      <h4>{emp_Id}</h4>

      <table border="3">
        <thead>
          <tr>
            <th>emp_Id</th>
            <th>ename</th>
            <th>gender</th>
          </tr>
        </thead>

        <tbody>
          {
            props.employees.map((emp) => (
              <tr key={emp.eid}>
                <td>{emp.eid}</td>
                <td>{emp.ename}</td>
                <td>{emp.gender}</td>
              </tr>
            ))
          }
        </tbody>
      </table>
    </div>
  )
}
export default CompB;
