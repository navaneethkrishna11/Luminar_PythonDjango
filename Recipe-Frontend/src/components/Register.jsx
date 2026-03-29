import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { userregister } from '../services/apicall';

const Register = () => {
  const[data,setData]=useState({username:'',email:'',password:''})
  const navigate = useNavigate()
  async function registered(e){
    e.preventDefault()
    let res = await userregister(data)
    navigate('/')
    
  }
  return (
    <div className="container d-flex justify-content-center align-items-center pt-4">
      <div className="card p-4 shadow" style={{ width: '400px' }}>
        <h3 className="text-center mb-4">Register</h3>

        <form onSubmit={registered}>
          <div className="mb-3">
            <label className="form-label">Full Name</label>
            <input
              type="text"
              className="form-control"
              placeholder="Enter full name"
              onChange={(e)=>{setData({...data,username:e.target.value})}}
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Email</label>
            <input
              type="email"
              className="form-control"
              placeholder="Enter email"
               onChange={(e)=>{setData({...data,email:e.target.value})}}
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Password</label>
            <input
              type="password"
              className="form-control"
              placeholder="Enter password"
               onChange={(e)=>{setData({...data,password:e.target.value})}}
            />
          </div>


          <button type="submit" className="btn btn-success w-100">
            Register
          </button>
        </form>

        <p className="text-center mt-3 mb-0">
          Already have an account? <a href="#">Login</a>
        </p>
      </div>
    </div>
  );
};

export default Register;