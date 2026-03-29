import React, { useState } from 'react'

const Counter = () => {
  const [count, setCount] = useState(0)
  // var count=0
  function increment(){
    setCount(count+1)
  }
  function decrement(){
    setCount(count-1)
  }
  function reset(){
   setCount(0)
  }

  return (
    <div className="container mt-5">
      <div className="card rounded-4 shadow p-5 text-center" style={{maxWidth: '500px', margin: '0 auto'}}>
        <h2 className="mb-4">Counter App</h2>
        
        <div className="display-1 fw-bold text-primary mb-4">
          {count}
        </div>
        
        <div className="d-flex gap-3 justify-content-center">
          <button 
            className="btn btn-danger btn-lg px-4" 
            onClick={decrement}
          >
            <strong>-</strong>
          </button>
          
          <button 
            className="btn btn-secondary btn-lg px-4" 
            onClick={reset}
          >
            Reset
          </button>
          
          <button 
            className="btn btn-success btn-lg px-4" 
            onClick={increment}
          >
            <strong>+</strong>
          </button>
        </div>
      </div>
    </div>
  )
}

export default Counter