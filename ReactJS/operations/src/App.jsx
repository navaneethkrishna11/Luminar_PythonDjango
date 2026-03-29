
import './App.css'
import Calculator from './components/Calculator'
import Counter from './components/Counter'
import Home from './components/Home'
import Navbar from './components/Navbar'
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import TempConverted from './components/TempConverted'
import BMI from './components/BMI'
import Hello from './components/Hello'

function App() {
  

  return (
    <>
      <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path='/' element={<Home/>}></Route>
        <Route path='/counter' element={<Counter/>}></Route>
        <Route path='/calculator' element={<Calculator/>}></Route>
        <Route path='/temp' element={<TempConverted/>}></Route>
        <Route path='/bmi' element={<BMI/>}></Route>
        <Route path='/hello' element={<Hello name='navanee' age='20'/>}></Route>
      </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
