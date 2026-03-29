import React from 'react'
import './App.css'
import Mycomponent from './components/Mycomponent'
import Navbar from './components/Navabr'
import Profile from './components/Profile'
import AboutMe from './components/About'
import Qualifications from './components/Qualifications'
import Skills from './components/Skills'

function App() {

  return (
    <>
    <Navbar/>
    <Profile/>
    <AboutMe/>
    <Qualifications/>
    <Skills/> 
    </>
  )
}

export default App
