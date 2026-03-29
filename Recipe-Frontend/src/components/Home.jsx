import React, { useEffect, useState } from 'react'
import { getallrecipes } from '../services/apicall'
import { useNavigate, useNavigation } from 'react-router-dom'

const Home = () => {

  const navigate=useNavigate()
  const [data, setData] = useState([])


  async function fetchrecipe() {
    try {
      const res = await getallrecipes()
      setData(res.data)
    
    } catch (error) {
      console.error(error)
    }
  }
  console.log(data)


  useEffect(() => {
    fetchrecipe()
  }, [])


  function addDetails(){
    navigate('/add')
  }

    function detail(i){
    navigate(`/details?id=${i}`)
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4 text-center">Recipes</h2>

      <div className="row">
        {data.map((item) => (
          <div className="col-md-4 mb-4" key={item.id}>
            <div className="card h-100 shadow-sm">
              <img
                src={item.image}
                className="card-img-top"
                alt={item.name}
                style={{ height: "200px", objectFit: "cover" }}
              />

              <div className="card-body">
                <h5 className="card-title text-center">{item.recipe_name}</h5>
                <p className="card-text">{item.description}</p>

                 <button
                            className="btn btn-sm btn-success me-2"
                            onClick={() => detail(item.id)}
                          >
                            View
                          </button>
              </div>
            </div>
          </div>
        ))}
      </div>
      <button className="btn btn-primary w-100" onClick={addDetails}> Add New Recipe</button>

    </div>
  )
}

export default Home
