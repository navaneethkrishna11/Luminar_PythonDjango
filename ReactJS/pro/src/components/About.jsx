import React from 'react'

const AboutMe = () => {
  return (
    <div className="container mt-5">
      <div className="card rounded-4 shadow p-4">
        <h2 className="text-center mb-4">About Me</h2>
        
        <div className="row g-3">
          <div className="col-md-4">
            <div className="p-3 border rounded">
              <strong>Name:</strong>
              <p className="mb-0 text-muted">John Doe</p>
            </div>
          </div>
          <div className="col-md-4">
            <div className="p-3 border rounded">
              <strong>Age:</strong>
              <p className="mb-0 text-muted">28 Years</p>
            </div>
          </div>
          <div className="col-md-4">
            <div className="p-3 border rounded">
              <strong>Location:</strong>
              <p className="mb-0 text-muted">New York, USA</p>
            </div>
          </div>
          
          <div className="col-md-4">
            <div className="p-3 border rounded">
              <strong>Email:</strong>
              <p className="mb-0 text-muted">john@example.com</p>
            </div>
          </div>
          <div className="col-md-4">
            <div className="p-3 border rounded">
              <strong>Phone:</strong>
              <p className="mb-0 text-muted">+1 234 567 8900</p>
            </div>
          </div>
          <div className="col-md-4">
            <div className="p-3 border rounded">
              <strong>Profession:</strong>
              <p className="mb-0 text-muted">Web Developer</p>
            </div>
          </div>
          
          <div className="col-md-4">
            <div className="p-3 border rounded">
              <strong>Experience:</strong>
              <p className="mb-0 text-muted">5+ Years</p>
            </div>
          </div>
          <div className="col-md-4">
            <div className="p-3 border rounded">
              <strong>Education:</strong>
              <p className="mb-0 text-muted">B.Sc Computer Science</p>
            </div>
          </div>
          <div className="col-md-4">
            <div className="p-3 border rounded">
              <strong>Languages:</strong>
              <p className="mb-0 text-muted">English, Spanish</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default AboutMe