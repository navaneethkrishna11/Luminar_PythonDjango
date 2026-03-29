import React, { useEffect,useState } from 'react'
import { useLocation } from 'react-router-dom'
import { getallbook } from '../services/ApiCall'
const Detail = () => {
  const[book,setBook] = useState({})
  const {search} = useLocation()
  console.log(search)
  const queryParams = new URLSearchParams(search)
  const i = queryParams.get('id')
  console.log(i)

  async function fetchbook(){
    let res = await getallbook(i)
    setBook(res.data)
 
  
  }
  useEffect(()=>{fetchbook(i)},[])

  return (
<div className="container mt-5">
  <div className="row justify-content-center">
    <div className="col-md-6">
      <div className="card border shadow-sm">
        <img 
          src={book.image} 
          className="card-img-top" 
          alt="Book cover"
          style={{ height: "300px", objectFit: "cover" }}
        />
        <div className="card-body text-center p-4">
           <h5 className="card-title mb-3">ID: {book.id}</h5>
          <h3 className="card-title text-primary mb-2">{book.name}</h3>
          <div className="border rounded p-3 bg-light">
            <p className="mb-0 fw-bold">
              <h4> AUTHOR : {book.author} <br/> Language : {book.language}</h4>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

  )
}

export default Detail
