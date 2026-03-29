import React, { useEffect, useState } from 'react'
import { allrecipeviews, deleterecipie, getrecipie } from '../services/apicall'
import { useLocation, useNavigate } from 'react-router-dom';

const Detail = () => {
  const [recipe,setRecipe] = useState();
  const[review,setReviews]= useState();
  const {search} = useLocation()
  console.log(search)
  const queryParams = new URLSearchParams(search)
  const i = queryParams.get('id')
  const navigate=useNavigate()

  async function fetchrecipie(){
    let res = await getrecipie(i)
    setRecipe(res.data)
  }  

  async function deletee(i){
  let res = await deleterecipie(i)
  navigate('/')
  }

    function editpage(i){
    navigate(`/edit?id=${i}`)
  }

  async function popup(){
    let res = await allrecipeviews(i)
    setReviews(res.data)
  }

  function addrev(){
    console.log('hello')
    navigate(`/addreview?id=${i}`)
  }


  useEffect(()=>{fetchrecipie()},[])
    return (
  <div className="container mt-5">
    {recipe && (
      <div className="row justify-content-center">
        <div className="col-md-8">
          <div className="card shadow">

            {/* Image */}
            <img
              src={recipe.image}
              className="card-img-top"
              alt={recipe.recipe_name}
              style={{ height: "300px", objectFit: "cover" }}
            />

            {/* Content */}
            <div className="card-body">
              <h3 className="card-title text-center mb-3">
                {recipe.recipe_name}
              </h3>

              <p className="card-text text-muted text-center">
                {recipe.instructions}
              </p>
              <p>
                Ingredients : {recipe.ingredients} <br/>
                Cusine :  {recipe.cusine} <br/>
               Meal type :  {recipe.mealtype}
              </p>

              {/* Buttons */}
              <div className="d-flex justify-content-between mt-4">
                <button className="btn btn-primary" onClick={()=>editpage(i)}>Edit</button>
                <button className="btn btn-danger" onClick={() => deletee(i)}>
                  Delete
                </button>
                <button className="btn btn-secondary" onClick={()=>popup(i)}>Reviews</button>
                <button className="btn btn-success" onClick={()=>addrev(i)}>Add Reviews</button>
              </div>
            </div>

            {review && review.map((i) => (
              <div  className="border p-2 mb-2">
                <p><strong>User Name : </strong> {i.user}</p>
                <p><strong>Recipe:</strong>{'*'.repeat(i.recipe)}</p>
                <p><strong>Rating:</strong> {i.rating}</p>
                <p><strong>Comment:</strong> {i.comment}</p>
                <hr></hr>
              </div>
            ))}


          </div>
        </div>
      </div>
    )}
  </div>
)
  
}

export default Detail
