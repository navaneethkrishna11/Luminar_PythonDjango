import React, { useState } from 'react'
import { postbook } from '../services/ApiCall'
import { useNavigate } from 'react-router-dom'

const Add = () => {

  const [data, setData] = useState({
    title: '',
    author: '',
    pages: '',
    price: '',
    language: '',
    image: null
  })

  const navigate = useNavigate()

  async function addbooks(e) {
    e.preventDefault()

    const formData = new FormData()
    formData.append('title', data.title)
    formData.append('author', data.author)
    formData.append('pages', data.pages)
    formData.append('price', data.price)
    formData.append('language', data.language)
    formData.append('image', data.image)

    await postbook(formData)
    navigate('/view')
  }

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8 col-lg-6">
          <div className="card shadow">
            <div className="card-header bg-success text-white">
              <h4>Add New Book</h4>
            </div>

            <form onSubmit={addbooks}>
              <div className="card-body">

                <input className="form-control mb-3"
                  placeholder="Book Title"
                  required
                  onChange={e => setData({...data, title: e.target.value})}
                />

                <input className="form-control mb-3"
                  placeholder="Author"
                  required
                  onChange={e => setData({...data, author: e.target.value})}
                />

                <input className="form-control mb-3"
                  placeholder="Pages"
                  required
                  onChange={e => setData({...data, pages: e.target.value})}
                />

                <input className="form-control mb-3"
                  placeholder="Price"
                  required
                  onChange={e => setData({...data, price: e.target.value})}
                />

                <input className="form-control mb-3"
                  placeholder="Language"
                  required
                  onChange={e => setData({...data, language: e.target.value})}
                />

                <input type="file"
                  className="form-control mb-4"
                  onChange={e => setData({...data, image: e.target.files[0]})}
                />

                <button type="submit" className="btn btn-success w-100">
                  Add Book
                </button>

              </div>
            </form>

          </div>
        </div>
      </div>
    </div>
  )
}

export default Add
