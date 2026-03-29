import axios from "axios"

export async function getallbooks()
{ 
    let t = localStorage.getItem('Token')
    let h={'Authorization':t}
    return await axios.get('http://127.0.0.1:8000/books/',{headers:h})
}

export async function postbook(data){
    let h = {'content-type' : 'multipart/form-data'}
    return await axios.post('http://127.0.0.1:8000/',data,{headers:h})
}

export async function getallbook(id)
{ 
    let t = localStorage.getItem('Token')
    let h={'Authorization':t}
    return await axios.get(`http://127.0.0.1:8000/books/${id}/`,{headers:h})
}
export async function editbook(id,data)
{ 
    let h = {'content-type' : 'multipart/form-data'}
    return await axios.put(`http://127.0.0.1:8000/books/${id}/`,data,{headers:h})
}

export async function bookdelete(id)
{ 
    return await axios.delete(`http://127.0.0.1:8000/books/${id}/`)
}

export async function searchbook(word)
{ 
    let p={'search':word}
    return await axios.get(`http://127.0.0.1:8000/search`,{params:p})
}

export async function userregister(data){
    return await axios.post('http://127.0.0.1:8000/users/',data)
}
export async function userlogin(data){
    return await axios.post('http://127.0.0.1:8000/login/',data)
}
export async function userlogout(){
    let t = localStorage.getItem('Token')
    let h={'Authorization':t}
    return await axios.get('http://127.0.0.1:8000/logout',{headers : h})
}