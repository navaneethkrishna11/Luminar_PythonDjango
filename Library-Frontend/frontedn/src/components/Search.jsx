import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import { searchbook } from '../services/apicall'

const Search = () => {
    const {search} = useLocation()
    const [ book, setBook]=useState([])
    const queryParams = new URLSearchParams(search)
    const word=queryParams.get('w')


    async function s(){
        let res = await searchbook(word)
        setBook(res.data)
    }
    useEffect(()=>{s()},[])

    console.log('book',book)

  return (
  <div className="container mt-4">
    <h2 className="text-center mb-4">Search Results</h2>

    {book.length === 0 ? (
      <div className="text-center text-muted">
        <div className="spinner-border" role="status"></div>
        <p className="mt-2">Loading books...</p>
      </div>
    ) : (
      <div className="row g-3">
        {book.map((b) => (
          <div className="col-md-4" key={b.id}>
            <div className="card h-100 shadow-sm">
              <img
                src={b.image}
                className="card-img-top"
                alt={b.name}
                style={{ height: '200px', objectFit: 'cover' }}
              />
              <div className="card-body">
                <h5 className="card-title">{b.name}</h5>
                <p className="card-text mb-1">
                  <strong>Author:</strong> {b.author}
                </p>
                <p className="card-text text-muted">
                  <strong>Language:</strong> {b.language}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    )}
  </div>
)
}

export default Search
