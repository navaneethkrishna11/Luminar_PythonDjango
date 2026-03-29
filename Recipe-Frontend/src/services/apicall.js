import axios from "axios";


export async function getallrecipes(){
    let t = localStorage.getItem('Token')
    let h={'Authorization':t}
    return await axios.get('http://127.0.0.1:8000/recipe/',{headers:h})
}

export async function getrecipie(id){
    let t = localStorage.getItem('Token')
    let h={'Authorization':t}
    return await axios.get(`http://127.0.0.1:8000/recipe/${id}/`,{headers:h})
}

export async function postrecipe(data){
     let h = {'content-type' : 'multipart/form-data'}
    return await axios.post('http://127.0.0.1:8000/recipe/',data,{headers:h})
}

export async function deleterecipie(id){
    return axios.delete(`http://127.0.0.1:8000/recipe/${id}/`)
}

export async function editrecipe(id,data)
{ 
    let h = {'content-type' : 'multipart/form-data'}
    return await axios.put(`http://127.0.0.1:8000/recipe/${id}/`,data,{headers:h})
}

export async function searchrecipe(word){
    let p={'search':word}
    return await axios.get('http://127.0.0.1:8000/search/',{params:p})
}

export async function userlogout(){
    let t = localStorage.getItem('Token')
    let h={'Authorization':t}
    return await axios.get('http://127.0.0.1:8000/logout',{headers : h})
}
export async function userlogin(data){
    return await axios.post('http://127.0.0.1:8000/login/',data)
}
export async function userregister(data){
    return await axios.post('http://127.0.0.1:8000/users/',data)
}

export async function allrecipeviews(i){
    return await axios.get((`http://127.0.0.1:8000/allreview/${i}`))
}
export async function createrecipe(data){
    let t = localStorage.getItem('Token')
    let h = {'Authorization':t}
    return await axios.post(`http://127.0.0.1:8000/review/`,data,{headers:h})
}