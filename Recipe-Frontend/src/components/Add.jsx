import React, { useState } from 'react'
import { postrecipe } from '../services/apicall'
import { useNavigate } from 'react-router-dom'



const Add = () => {
  const navigate=useNavigate()

  const [data, setData] = useState({
    recipe_name: '',
    instructions: '',
    ingredients: '',
    cusine:'',
    mealtype:'',
    image: null
  })

  async function add(event){
    event.preventDefault()
    let res = await postrecipe(data)
    navigate('/')
  }

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8 col-lg-6">
          <div className="card shadow">
            <div className="card-header bg-success text-white">
              <h4>Add New Recipe</h4>
            </div>

            <form onSubmit={add} >
              <div className="card-body">

                <input className="form-control mb-3"
                  placeholder="Recipe Title"
                  required
                  onChange={e => setData({...data, recipe_name: e.target.value})}
                />

                <textarea className="form-control mb-3"
                  placeholder='instructions'
                  required
                  onChange={e => setData({...data, instructions: e.target.value})}
                ></textarea>

                <textarea className="form-control mb-3"
                  placeholder="ingredients"
                  required
                  onChange={e => setData({...data, ingredients: e.target.value})}
                ></textarea>

                <input className="form-control mb-3"
                  placeholder="meal type"
                  required
                  onChange={e => setData({...data, mealtype: e.target.value})}
                />

                <input className="form-control mb-3"
                  placeholder="cusine"
                  required
                  onChange={e => setData({...data, cusine: e.target.value})}
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
