import React,{useState} from 'react';
import { userlogin } from '../services/apicall';
import { useNavigate } from 'react-router-dom';

const Login = ({fun}) => {
  const [data,setData] = useState({username:'',password:''})
  const navigate = useNavigate()
  
  async function logined(e){
    e.preventDefault()
    let res = await userlogin(data)
     // console.log(data)
     let t = res.data['token']
     console.log('before',localStorage.getItem('Token'))
     
     localStorage.setItem('Token','token '+t)
     console.log('after',localStorage.getItem('Token'))
     navigate('/')
     fun()
     
  }
  return (
    <div className="container d-flex justify-content-center align-items-center pt-4">
      <div className="card p-4 shadow" style={{ width: '350px' }}>
        <h3 className="text-center mb-4">Login</h3>

        <form onSubmit={logined}>
          <div className="mb-3">
            <label className="form-label">Username </label>
            <input
              type="text"
              className="form-control"
              placeholder="Enter email"
              onChange={(e)=>{setData({...data,username:e.target.value})}}
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
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;