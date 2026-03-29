import { useState } from "react";
import React from 'react';
import { userregister } from "../services/apicall";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [data,setData]=useState({username:'',email:'',password:'',})
  const navigate= useNavigate()

  async function register(e){
    e.preventDefault()
    await userregister(data)
    navigate('/')

  }


  return (
    <div className="container d-flex justify-content-center align-items-center vh-100">
      <div className="card p-4 shadow" style={{ width: '400px' }}>
        <h3 className="text-center mb-4">Register</h3>

        <form onSubmit={register}>
          <div className="mb-3">
            <label className="form-label">Full Name</label>
            <input
              type="text"
              className="form-control"
              placeholder="Enter full name"
              onChange={(event)=>{setData({...data,username:event.target.value})}}
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Email</label>
            <input
              type="email"
              className="form-control"
              placeholder="Enter email"
              onChange={(event)=>{setData({...data,email:event.target.value})}}

            />
          </div>

          <div className="mb-3">
            <label className="form-label">Password</label>
            <input
              type="password"
              className="form-control"
              placeholder="Enter password"
              onChange={(event)=>{setData({...data,password:event.target.value})}}

            />
          </div>

          {/* <div className="mb-3">
            <label className="form-label">Confirm Password</label>
            <input
              type="password"
              className="form-control"
              placeholder="Confirm password"
            />
          </div> */}

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