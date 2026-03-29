import React, { useEffect,useState } from 'react'
import {getallbooks,bookdelete,editbook} from '../services/ApiCall'
import { useNavigate } from 'react-router-dom'

const View = () => {

  const [books,setBooks]= useState([])
  const navigate=useNavigate()
  
  async function fetchbooks(){
    let res = await getallbooks()
    setBooks(res.data)

  }
  function detail(i){
    navigate(`/details?id=${i}`)
  }
    function editbook(i){
    navigate(`/edit?id=${i}`)
  }
  async function deletebook(i){
    let res= await bookdelete(i)
    fetchbooks()

  }

  useEffect(()=>{
    fetchbooks(),[]})

  return (
 <div className="container mt-5">
        <div className="row">
          <div className="col-12">
            <div className="card shadow-lg border-0 ">
              <div className="card-header bg-success text-white py-3">
                <h3 className="mb-0"> Book Library</h3>
              </div>
              <div className="card-body p-0">
                <div className="table-responsive">
                  <table className="table table-hover table-striped mb-0">
                    <thead className="table-dark">
                      <tr>
                        <th scope="col">Image</th>
                        <th scope="col">Book Name</th>
                        <th scope="col">Author</th>
                        <th scope="col">Price</th>
                        <th scope="col">Language</th>
                        <th scope='col'>Actions</th>
                      </tr>
                    </thead>
                  {books.map((i)=>
                    <tr>
                      <td><img src={i.image} height='100px' width='90px' /></td>
                      <td>{i.name}</td>
                      <td>{i.author}</td>
                      <td>{i.price}</td>
                      <td>{i.language}</td>
                     <td td>
                          <button
                            className="btn btn-sm btn-info me-2"
                            onClick={() => detail(i.id)}
                          >
                            View
                          </button>

                          <button
                            className="btn btn-sm btn-danger me-2"
                            onClick={() => deletebook(i.id)}
                          >
                            Delete
                          </button>
                          
                          <button
                            className="btn btn-sm btn-danger"
                            onClick={() => editbook(i.id)}
                          >
                            Edit
                          </button>
                          </td>
                    </tr>
                  )}
                  </table>
              </div>
            </div>
          </div>
        </div>
      </div>
      </div>
  )
}

export default View
