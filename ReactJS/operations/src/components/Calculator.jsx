import React, { useState } from 'react'

const Calculator = () => {
    const [num1,setNum1] = useState(0)
    const [num2,setNum2] = useState(0)
    const [result,setResult] = useState()

    // function input1(){
    //     setNum1(event.target.value)
    // }
    // function input2(){
    //     setNum2(event.target.value)
    // }
    function add(){
        let r = Number(num1)+Number(num2)
        setResult(r)
    }
    function sub(){
        let r = Number(num1)-Number(num2)
        setResult(r)
    }
    function pdt(){
        let r = Number(num1)*Number(num2)
        setResult(r)
    }
    function div(){
        let r = Number(num1)/Number(num2)
        setResult(r)
    }
  return (
    <div className="container mt-5">
      <div className="card rounded-4 shadow p-4" style={{maxWidth: '400px', margin: '0 auto'}}>
        <h3 className="text-center mb-4">Calculator</h3>
        
        <div className="mb-3">
          <label className="form-label">Number 1</label>
          <input type="number" className="form-control" placeholder="Enter first number" onChange={()=>setNum1(event.target.value)}/>
        </div>
        
        <div className="mb-3">
          <label className="form-label">Number 2</label>
          <input type="number" className="form-control" placeholder="Enter second number" onChange={()=>setNum2(event.target.value)} />
        </div>
        
        <div className="mb-3">
          <label className="form-label">Operation</label>
          <div className="row g-2">
            <div className="col-3">
              <button className="btn btn-primary w-100" onClick={add}>+</button>
            </div>
            <div className="col-3">
              <button className="btn btn-primary w-100" onClick={sub}>-</button>
            </div>
            <div className="col-3">
              <button className="btn btn-primary w-100" onClick={pdt}>×</button>
            </div>
            <div className="col-3">
              <button className="btn btn-primary w-100" onClick={div}>÷</button>
            </div>
          </div>
        </div>
        
        <div className="alert alert-info text-center">
          <strong >Result: {result}</strong>
        </div>
      </div>
    </div>
  )
}

export default Calculator