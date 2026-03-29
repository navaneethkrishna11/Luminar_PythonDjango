import './App.css'
import Footer from './components/Footer'
import Navbar from './components/Navbar'
import Auth from './pages/Auth'
import Home from './pages/Home'
import {BrowserRouter,Route,Routes} from 'react-router-dom'
import Service from './pages/service/service'
import Customer from './pages/customer/customer'

function App() {

  return (
    <>
      <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path='/' element={<Home/>}></Route>
        <Route path='/auth' element={<Auth/>}></Route>
        <Route path='/service' element={<Service/>}></Route>
        <Route path='/customer' element={<Customer/>}></Route>

      </Routes>
      <Footer/>
      </BrowserRouter>
    </>
  )
}

export default App
