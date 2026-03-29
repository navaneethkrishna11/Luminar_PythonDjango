import React, { useState,useContext } from 'react'
import { useNavigate } from 'react-router-dom'
import { userlogin, userregister,getCurrentUser } from '../services/apicall'
import { AuthContext } from "../context/AuthContext"

const Field = ({ label, name, type = 'text', placeholder, value, onChange }) => (
  <div>
    <label className="block text-xs font-semibold text-slate-500 mb-1.5 tracking-wide">{label}</label>
    <input
      name={name} type={type} placeholder={placeholder}
      value={value} onChange={onChange} required
      className="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-white text-sm text-[#0C2C55] placeholder:text-slate-300 outline-none focus:border-[#629FAD] focus:shadow-[0_0_0_3px_rgba(98,159,173,0.10)] transition-all"
    />
  </div>
)

export default function Auth() {
  const [mode, setMode] = useState('login')

  const [login, setLogin] = useState({ username: '', password: '' })
  const [reg, setReg] = useState({ username: '', email: '', password: '', place: '', pincode: '', role: '' })

  const setL = e => setLogin(p => ({ ...p, [e.target.name]: e.target.value }))
  const setR = e => setReg(p => ({ ...p, [e.target.name]: e.target.value }))

  const { loginUser } = useContext(AuthContext)

  const navigate = useNavigate()
  async function registered(e){
    e.preventDefault()
    let res = await userregister(reg)
    navigate('/auth')
    
  }

    async function logined(e){
  e.preventDefault()

  let res = await userlogin(login)
  const me = await getCurrentUser(); 

  loginUser(res.data) 
  

  if(me.data.role === 'customer'){
      navigate('/customer')
  } 
  else if(me.data.role === 'service_provider'){
      navigate('/service')
  }
}

  return (
    <div className="min-h-screen flex items-center justify-center bg-[#F2F2E6] px-4 py-22">
      <div className="w-full max-w-md">

        {/* Logo */}
        <a href="/" style={{ textDecoration: 'none' }}
          className="font-['Cormorant_Garamond'] text-3xl font-bold text-[#0C2C55] block text-center mb-8">
         
        </a>

        {/* Card */}
        <div className="bg-white rounded-3xl border border-slate-200/80 shadow-[0_8px_40px_rgba(12,44,85,0.08)] p-8">

          {/* Toggle */}
          <div className="flex bg-slate-100 rounded-full p-1 mb-7">
            {['login', 'register'].map(m => (
              <button key={m} onClick={() => setMode(m)}
                className={`flex-1 py-2 rounded-full text-sm font-semibold transition-all ${
                  mode === m ? 'bg-[#0C2C55] text-white shadow-sm' : 'text-slate-400 hover:text-slate-600'
                }`}>
                {m === 'login' ? 'Log in' : 'Sign up'}
              </button>
            ))}
          </div>

          {/* LOGIN */}
          {mode === 'login' && (
            <form className="space-y-4" onSubmit={logined}>
              <Field label="Username" name="username" placeholder="your_username" value={login.username} onChange={setL} />
              <Field label="Password" name="password" type="password" placeholder="••••••••" value={login.password} onChange={setL} />
              <a href="#" style={{ textDecoration: 'none' }} className="block text-right text-xs text-[#629FAD] hover:text-[#296374] -mt-1">
                Forgot password?
              </a>
              <button type="submit"
                className="w-full bg-[#0C2C55] hover:bg-[#1a3d6e] text-white text-sm font-semibold py-3 rounded-xl transition-all hover:-translate-y-px shadow-sm mt-1">
                Log in →
              </button>
            </form>
          )}

          {/* REGISTER */}
          {mode === 'register' && (
            <form className="space-y-3.5" onSubmit={registered}>
              <Field label="Username" name="username" placeholder="your_username" value={reg.username} onChange={setR} />
              <Field label="Email" name="email" type="email" placeholder="you@example.com" value={reg.email} onChange={setR} />
              <Field label="Password" name="password" type="password" placeholder="••••••••" value={reg.password} onChange={setR} />
              <div className="grid grid-cols-2 gap-3">
                <Field label="Place" name="place" placeholder="City / Town" value={reg.place} onChange={setR} />
                <Field label="Pincode" name="pincode" placeholder="682001" value={reg.pincode} onChange={setR} />
              </div>
              <div>
                <label className="block text-xs font-semibold text-slate-500 mb-1.5 tracking-wide">Role</label>
                <select name="role" value={reg.role} onChange={setR} required
                  className="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-white text-sm text-[#0C2C55] outline-none focus:border-[#629FAD] focus:shadow-[0_0_0_3px_rgba(98,159,173,0.10)] transition-all appearance-none cursor-pointer">
                  <option value="" disabled>Select your role</option>
                  <option value="customer">Customer</option>
                  <option value="service_provider">Service Provider</option>
                </select>
              </div>
              <button type="submit"
                className="w-full bg-[#0C2C55] hover:bg-[#1a3d6e] text-white text-sm font-semibold py-3 rounded-xl transition-all hover:-translate-y-px shadow-sm mt-1">
                Create account →
              </button>
            </form>
          )}

          {/* Switch */}
          <p className="text-center text-xs text-slate-400 mt-6">
            {mode === 'login' ? "Don't have an account? " : 'Already have an account? '}
            <button onClick={() => setMode(mode === 'login' ? 'register' : 'login')}
              className="text-[#296374] font-semibold hover:text-[#0C2C55] transition-colors">
              {mode === 'login' ? 'Sign up' : 'Log in'}
            </button>
          </p>

        </div>

        <p className="text-center text-xs text-slate-400 mt-6">
          Every service · One platform · <span className="text-[#629FAD]">BookUp</span>
        </p>
      </div>
    </div>
  )
}