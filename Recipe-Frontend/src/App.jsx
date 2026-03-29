
import { BrowserRouter,Routes,Route } from 'react-router-dom'
import './App.css'
import Navbar from './components/Navbar'
import Home from './components/Home'
import Add from './components/Add'
import Detail from './components/Detail'
import Edit from './components/Edit'
import Register from './components/Register'
import Login from './components/Login'
import Search from './components/Search'
import { useEffect, useState } from 'react'
import Addreview from './components/Addreview'
function App() {
  const [islog,setlog] = useState()
  function loginstatus (){
    let t = localStorage.getItem('Token')
    setlog(!(!(t)))
  }

  useEffect(()=>{loginstatus()},[])
  

  return (
    <>
      <BrowserRouter>
      <Navbar fun={loginstatus} islogin={islog}/>
      <Routes>
        <Route path='/' element={<Home/>}></Route>
        <Route path='/add' element={<Add/>}></Route>
        <Route path='/details' element={<Detail/>}></Route>
        <Route path='/edit' element={<Edit/>}></Route>
        <Route path='/register' element={<Register/>}></Route>
        <Route path='/login' element={<Login/>}></Route>
        <Route path='/search' element={<Search/>}></Route>
         <Route path='/addreview' element={<Addreview/>}></Route>
      </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
