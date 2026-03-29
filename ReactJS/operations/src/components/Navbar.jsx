import React from 'react'
import { Link } from 'react-router-dom'
const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container">
        <a className="navbar-brand" href="#home">Counter</a>
        <button 
          className="navbar-toggler" 
          type="button" 
          data-bs-toggle="collapse" 
          data-bs-target="#navbarNav"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">
            <li className="nav-item"> 
              <Link to='/'>
              <a className="nav-link active" href="#home">Home</a>
              </Link>
            </li>
            <li className="nav-item">
              <Link to='counter'>
              <a className="nav-link" href="#about">Counter</a>
              </Link>
            </li>
             <li className="nav-item">
              <Link to='calculator'>
              <a className="nav-link" href="#about">Calculator</a>
              </Link>
            </li>
            <li className="nav-item">
              <Link to='temp'>
              <a className="nav-link" href="#about">TempConvert</a>
              </Link>
            </li>
              <li className="nav-item">
              <Link to='bmi'>
              <a className="nav-link" href="#about">BMI</a>
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Navbar