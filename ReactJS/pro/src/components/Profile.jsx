import React from 'react'
import p1 from '../assets/images/p1.png'

const Profile = () => {
    var x = 'John Doe';
    var a ={'name':'navanee','age':20,'place':'tirur'};
  return (
    <div className="container mt-5">
      <div className="card rounded-4 shadow p-4">
        <div className="row align-items-center">
          <div className="col-md-8">
            <h2 className="mb-3"> {x}</h2>
            <p className="text-muted">
              Hello! I'm a passionate web developer with over 5 years of experience 
              in creating beautiful and functional websites. I specialize in React, 
              Node.js, and modern web technologies. I love turning complex problems 
              into simple, beautiful, and intuitive designs.
              <br/>
              Age : {a.age} 

            </p>
            <p className="text-muted">
              When I'm not coding, you can find me exploring new technologies, 
              reading tech blogs, or enjoying a good cup of coffee while brainstorming 
              my next project.
            </p>
          </div>
          <div className="col-md-4 text-center">
            <div className="rounded-circle border border-3 border-black overflow-hidden mx-auto" 
                 style={{width: '200px', height: '200px'}}>
              <img 
                src={p1}
                alt="Profile" 
                className="w-100 h-100 object-fit-cover"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Profile;