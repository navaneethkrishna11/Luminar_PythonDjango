import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { userlogout } from '../services/apicall';

const Navbar = ({islogin,fun}) => {
  const [ word,setWord] =useState()
  const navigate = useNavigate()

  function searchbar(){
    navigate(`/search?w=${word}`)
    console.log(word)
  }

  async function loggout(){
   let res = await userlogout()
   console.log(res)
   localStorage.clear()
   navigate('/')
   fun()
   
  }
  return (
    <nav
      className="navbar navbar-expand-lg shadow"
      style={{
        backgroundColor: '#9ACD32', // yellow-green
        minHeight: '80px'
      }}
    >
      <div className="container-fluid px-4">

        {/* Left - Brand */}
        <a
          className="navbar-brand fw-bold text-dark"
          href="/add"
          style={{ fontSize: '1.4rem' }}
        >
          🍽 Recipe Manager
        </a>

        {/* Toggler */}
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Center - Nav Links */}
        <div
          className="collapse navbar-collapse justify-content-center"
          id="navbarSupportedContent"
        >
          <ul className="navbar-nav gap-4">
            <li className="nav-item">
              <a className="nav-link fw-semibold text-dark" href="/">Home</a>
            </li>
             {islogin &&
             <>
             <li className="nav-item">
              <a className="nav-link fw-semibold text-dark" href="/add">Add</a>
            </li>
             <li className="nav-item">
              <a className="nav-link fw-semibold text-dark" href="#" onClick={loggout}>Logout</a>
            </li>
            </>
              }
            {!islogin &&
            <>
            <li className="nav-item">
              <a className="nav-link fw-semibold text-dark" href="/register">Register</a>
            </li>
            <li className="nav-item">
              <a className="nav-link fw-semibold text-dark" href="/login">Login</a>
            </li>
            <li className="nav-item">
              <a className="nav-link fw-semibold text-dark" href="/register">Register</a>
            </li>
            </>}
          </ul>
        </div>

        {/* Right - Search */}
        <div className="d-flex">
          <input
            className="form-control me-2 rounded-pill"
            type="search"
            placeholder="Search recipes..."
            onChange={(event)=>{setWord(event.target.value)}}
          />
          <button
            className="btn btn-dark rounded-pill px-4"
            type="submit"
            onClick={searchbar}
          >
            Search
          </button>
        </div>

      </div>
    </nav>
  );
};

export default Navbar;