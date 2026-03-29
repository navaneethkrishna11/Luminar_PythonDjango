import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { createrecipe } from "../services/apicall";

const Addreview = () => {
  const [data, setData] = useState({ recipe :'',rating: "", comment: "",user:'' });
  const {search} = useLocation()
  console.log(search)
  const queryParams = new URLSearchParams(search)
  const i = queryParams.get('id')
  const navigate=useNavigate()

  async function addcomment(e) {
    e.preventDefault();
    console.log(data);
    data.recipe=i
    data.user=2
    console.log(data)
    let res = await createrecipe(data)
    console.log(res)
    navigate(`/details?id=${i}`)
  }

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">

          <div className="card shadow-lg border-0">
            <div className="card-body p-4">
              <h4 className="text-center mb-4 text-success">
                Add Your Review
              </h4>

              <form onSubmit={addcomment}>
                
                {/* Rating */}
                <div className="mb-3">
                  <label className="form-label fw-semibold">
                    Rating (1 to 5)
                  </label>
                  <input
                    type="number"
                    className="form-control"
                    min="1"
                    max="5"
                    placeholder="Enter rating"
                    value={data.rating}
                    onChange={(e) =>
                      setData({ ...data, rating: e.target.value })
                    }
                    required
                  />
                </div>

                {/* Comment */}
                <div className="mb-3">
                  <label className="form-label fw-semibold">
                    Comment
                  </label>
                  <textarea
                    className="form-control"
                    rows="4"
                    placeholder="Write your review..."
                    value={data.comment}
                    onChange={(e) =>
                      setData({ ...data, comment: e.target.value })
                    }
                    required
                  ></textarea>
                </div>

                {/* Submit */}
                <div className="d-grid">
                  <button type="submit" className="btn btn-success">
                    Submit Review
                  </button>
                </div>

              </form>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
};

export default Addreview;
