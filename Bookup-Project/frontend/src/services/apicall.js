import axios from "axios";

// Slot data
export async function getallslot(){
    let t = localStorage.getItem('Token')
    let h={'Authorization':t}
    return await axios.get('http://127.0.0.1:8000/slot/',{headers:h})
}

export async function getslot(id){
    let t = localStorage.getItem('Token')
    let h={'Authorization':t}
    return await axios.get(`http://127.0.0.1:8000/slot/${id}/`,{headers:h})
}

export async function addservice(data){
     let h = {'content-type' : 'multipart/form-data'}
    return await axios.post('http://127.0.0.1:8000/slot/',data,{headers:h})
}

export async function deleteservice(id){
    return axios.delete(`http://127.0.0.1:8000/slot/${id}/`)
}

export async function editslot(id,data)
{ 
    let h = {'content-type' : 'multipart/form-data'}
    return await axios.put(`http://127.0.0.1:8000/slot/${id}/`,data,{headers:h})
}

export async function searchslot(word){
    let p={'search':word}
    return await axios.get('http://127.0.0.1:8000/slot/',{params:p})
}

// User auth
export async function userlogout(){
    let t = localStorage.getItem('Token')
    let h={'Authorization':t}
    return await axios.get('http://127.0.0.1:8000/logout',{headers : h})
}
export async function userlogin(data) {
  const res = await axios.post("http://127.0.0.1:8000/login/", data);
  // if backend returns: { token: "9944b091..." }
  localStorage.setItem("Token", "Token " + res.data.token);
  return res;
}
export async function userregister(data){
    return await axios.post('http://127.0.0.1:8000/users/',data)
}

export async function getCurrentUser() {
  let t = localStorage.getItem("Token");
  let h = { Authorization: t };
  return await axios.get("http://127.0.0.1:8000/me/", { headers: h });
}


export async function createrecipe(data){
    let t = localStorage.getItem('Token')
    let h = {'Authorization':t}
    return await axios.post(`http://127.0.0.1:8000/review/`,data,{headers:h})
}

// booking data
export async function bookSlot(data) {
  return await axios.post('http://127.0.0.1:8000/book/', data);
}