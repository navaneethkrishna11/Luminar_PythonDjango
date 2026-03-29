import React, { useState,useEffect } from 'react'
import { editbook, getallbook } from '../services/ApiCall'
import { useLocation } from 'react-router-dom'
import { useNavigate } from 'react-router-dom'


const Edit = () => {
  const {search} = useLocation()
  const queryParams = new URLSearchParams(search)
  const i = queryParams.get('id')
  // const navigate=useNavigate()

  const [data, setData] = useState({
    name: '',
    author: '',
    page: '',
    price: '',
    language: '',
    image: ''
  })

    async function fetchbook(){
    let res = await getallbook(i)
    setData(res.data)
  }


  async function updatebook(e) {
    console.log(data)
    e.preventDefault()
    let book={...data}
    if(typeof(book.image)=="string")
    {
      delete book.image
    }
    // let res = await editbook(i,data)
    // navigate('/view')

  
  }
  
    useEffect(()=>{fetchbook()},[])

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8 col-lg-6">
          <div className="card shadow">
            <div className="card-header bg-success text-white">
              <h4>Add New Book</h4>
            </div>

            <form onSubmit={updatebook}>
              <div className="card-body">

                <input className="form-control mb-3"
                  placeholder="Book Title"
                  value={data.name}
                  onChange={e => setData({...data, name: e.target.value})}
                />

                <input className="form-control mb-3"
                  placeholder="Author"
                  value={data.author}
                  onChange={e => setData({...data, author: e.target.value})}
                />

                <input className="form-control mb-3"
                  placeholder="Pages"
                  value={data.page}
                  onChange={e => setData({...data, page: e.target.value})}
                />

                <input className="form-control mb-3"
                  placeholder="Price"
                  value={data.price}
                  onChange={e => setData({...data, price: e.target.value})}
                />

                <input className="form-control mb-3"
                  placeholder="Language"
                  value={data.language}
                  onChange={e => setData({...data, language: e.target.value})}
                />

                <input type="file"
                  className="form-control mb-4"
                  
                  onChange={e => setData({...data, image: e.target.files[0]})}
                />

                <button type="submit" className="btn btn-success w-100">
                  save
                </button>

              </div>
            </form>

          </div>
        </div>
      </div>
    </div>
  )
}

export default Edit
