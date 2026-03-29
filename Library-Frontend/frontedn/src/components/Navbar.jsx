import React from 'react';
import  { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { userlogout } from '../services/apicall';

const Navbar = ({islog,fun}) => {
  const [ word,setWord] =useState()
  const navigate = useNavigate()

  function searchbar(){
    navigate(`/search?w=${word}`)
    console.log(word)
  }
  async function logouted(){
   let res = await userlogout()
   console.log(res)
   localStorage.clear()
   fun()
   navigate('/')
  }
  return (
    <>
      <link 
        href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css" 
        rel="stylesheet"
      />
      
      <style>{`
        .navbar {
          position: fixed;
          top: 0;
          width: 100%;
          z-index: 1000;
          box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        body {
          padding-top: 70px;
        }
      `}</style>

      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">Library</a>
          <button 
            className="navbar-toggler" 
            type="button" 
            data-bs-toggle="collapse" 
            data-bs-target="#navbarSupportedContent" 
            aria-controls="navbarSupportedContent" 
            aria-expanded="false" 
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <a className="nav-link active" aria-current="page" href="/">Home</a>
              </li>
              {islog && 
              <>
              <li className="nav-item">
                <a className="nav-link" href="/view">View</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/add">Add</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" style={{cursor:'pointer'}} onClick={logouted}>Logout</a>
              </li>
              </>
              }

              {!islog &&
              <>
              <li className="nav-item">
                <a className="nav-link" href="/register">Register</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/login">Login</a>
              </li>
              </>
              }

            </ul>
            <div className="d-flex">
              <input 
                className="form-control me-2" 
                type="search" 
                placeholder="Search" 
                aria-label="Search"
                onChange={(event)=>{setWord(event.target.value)}}

              />
              <button className="btn btn-outline-success" type="button" onClick={searchbar}>Search</button>
            </div>
          </div>
        </div>
      </nav>
      

    </>
  );
};

export default Navbar;