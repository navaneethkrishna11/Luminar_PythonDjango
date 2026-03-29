import React,{useState} from 'react'

const BMI = () => {
    const [ data,setData]=useState({'height':'','weight':''})
    const[result,setResult]=useState(0)
    function calculate(){
        console.log(data)
        let r=(data.weight/(data.height /100)**2)
        setResult(r)

    }
  return (
    <div>
        <div className="container mt-5">
        <div className="card rounded-4 shadow p-4" style={{maxWidth: '400px', margin: '0 auto'}}>
        <h3 className="text-center mb-4">BMI</h3>
          <div className="mb-3">
          <label className="form-label">Hieght in KG</label>
          <input type="number" className="form-control" placeholder="Enter first number" onChange={()=> setData({...data,'height':event.target.value})}/>
        </div>
        
        <div className="mb-3">
          <label className="form-label">Weight in cm</label>
          <input type="number" className="form-control" placeholder="Enter second number" onChange={()=>setData({...data,'weight':event.target.value})} />
        </div>

        <div className="col-3">
              <button className="btn btn-primary w-100" onClick={calculate}>calculate</button>
            </div>

       <div className="alert alert-info text-center">
          <strong >BMI : {result}</strong>
        </div>
        </div>
        </div>
      
    </div>
  )
}

export default BMI
