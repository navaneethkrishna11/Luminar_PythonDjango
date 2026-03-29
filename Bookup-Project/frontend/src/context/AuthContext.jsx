import { createContext, useState, useEffect } from "react"

export const AuthContext = createContext()

export const AuthProvider = ({ children }) => {

  const [auth, setAuth] = useState({
    token: null,
    role: null,
    userId: null,
    username:null
  })

  useEffect(() => {
    const token = localStorage.getItem("Token")
    const role = localStorage.getItem("Role")
    const userId = localStorage.getItem("UserId")
    const username = localStorage.getItem('name')

    if(token){
      setAuth({ token, role, userId,username })
    }
  }, [])

  const loginUser = (data) => {
    localStorage.setItem("Token", "token " + data.token)
    localStorage.setItem("Role", data.role)
    localStorage.setItem("UserId", data.id)
    localStorage.setItem('Username',data.name)


    setAuth({
      token: data.token,
      role: data.role,
      userId: data.id,
      username:data.name
    })
  }

  console.log(auth)

  const logoutUser = () => {
    localStorage.clear()
    setAuth({ token: null, role: null, userId: null,username:null })
  }

  return (
    <AuthContext.Provider value={{ auth, loginUser, logoutUser }}>
      {children}
    </AuthContext.Provider>
  )
}