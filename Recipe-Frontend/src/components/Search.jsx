import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import { searchrecipe } from '../services/apicall'

const Search = () => {
    const {search} = useLocation()
    const [ book, setBook]=useState()
    const queryParams = new URLSearchParams(search)
    const word=queryParams.get('w')
    console.log('word ferthced',word)

    async function searchbook(){
        let res = await searchrecipe(word)
        console.log(res.data)
    }
    useEffect(()=>{searchbook()},[])

  return (
    <div>
      <h1>Search</h1>
    </div>
  )
}

export default Search
