import React, { useEffect, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import {  editrecipe, getrecipie } from '../services/apicall'

const Edit = () => {
    const [data,setData] = useState({'recipe_name':'','instructions':'','cusine':'','mealtype':'','image':''})
const {search} = useLocation()
  const navigate=useNavigate()
  const queryParams = new URLSearchParams(search)
  const i = queryParams.get('id')

      async function fetchrecipie(){
        let res = await getrecipie(i)
        setData(res.data)
      }  
      console.log(data)

    async function updaterecipe(event)
    {
     event.preventDefault()
    let book={...data}
    if(typeof(book.image)=="string")
    {
      delete book.image
    }
    let res = await editrecipe(i,data)
    navigate('/view')

        console.log('ok')
    }

    useEffect(()=>{fetchrecipie()},[])
 return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8 col-lg-6">
          <div className="card shadow">
            <div className="card-header bg-success text-white">
              <h4>Add New Recipe</h4>
            </div>

            <form onSubmit={updaterecipe}>
              <div className="card-body">

                <input className="form-control mb-3"
                  placeholder="Recipe Name"
                  value={data.recipe_name}
                  onChange={e => setData({...data, recipe_name: e.target.value})}
                />

                <textarea className="form-control mb-3"
                  placeholder="Instructions"
                  value={data.instructions}
                  onChange={e => setData({...data, instructions: e.target.value})}
                >
                </textarea>

                <input className="form-control mb-3"
                  placeholder="cusine"
                  value={data.cusine}
                  onChange={e => setData({...data, cusine: e.target.value})}
                />

                <input className="form-control mb-3"
                  placeholder="meal type"
                  value={data.mealtype}
                  onChange={e => setData({...data, mealtype: e.target.value})}
                />


                <input type="file"
                  className="form-control mb-4"
                  
                  onChange={e => setData({...data, image: e.target.files[0]})}
                />

                <button type="submit" className="btn btn-success w-100">
                  Update
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
