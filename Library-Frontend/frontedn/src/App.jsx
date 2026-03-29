
import { BrowserRouter, Route, Routes } from 'react-router-dom'

import Navbar from './components/Navbar'
import Add from './components/Add'
import View from './components/View'
import Update from './components/Update'
import Register from './components/Register'
import Login from './components/Login'
import Detail from './components/Detail'
import Edit from './components/Edit'
import Search from './components/Search'
import Home from './components/Home'
import { useEffect, useState } from 'react'

function App() {
  const[islog,setlog]=useState(false)

  function checkloginstatus(){
    let t = localStorage.getItem('Token')
    console.log(t)
    setlog(!(!(t)))
  }

  useEffect(()=>{checkloginstatus()},[])
  return (
    <>
    <BrowserRouter>
    <Navbar islog={islog} fun={checkloginstatus}/>
      <Routes>
        <Route path='/' element={<Home/>}></Route>
        <Route path='/view' element={<View/>} ></Route>
        <Route path='/add' element={<Add/>} ></Route>
        <Route path='/update' element={<Update/>} ></Route>
        <Route path='/register' element={<Register/>} ></Route>
        <Route path='/login' element={<Login fun={checkloginstatus}/>} ></Route>
        <Route path='/details' element={<Detail/>} ></Route>
        <Route path='/edit' element={<Edit/>}></Route>
        <Route path='/search' element={<Search/>}></Route>
       
      </Routes>
    
    </BrowserRouter>
      
       
    </>
  )
}

export default App
