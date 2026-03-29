import React, { useState } from 'react'

const TempConverted = () => {
    const [ result,setResult] = useState(0)
    const [num1,setNum1]=useState(0)
    function input(){
        setResult('')
        setNum1(event.target.value)
    }
    function convert(){
        let r= (Number(num1) * 1.8) + 32;
        setResult(r)
    }
  return (
    <div className="container mt-5">
      <div className="card shadow-sm p-4">

        <h3 className="text-center text-primary mb-4">
          Temperature Converter
        </h3>

        <div className="mb-3">
          <label className="form-label">Enter Temperature in Celsius</label>
          <input
            type="number"
            className="form-control"
            placeholder="Enter value"
            onChange={input}
          />
        </div>

        <div className="d-grid mb-3">
          <button className="btn btn-primary" onClick={convert}>
            Convert
          </button>
        </div>

        <div className="text-center fw-bold">
          Output in farnheit : {result}
        </div>

      </div>
    </div>
  )
}

export default TempConverted
