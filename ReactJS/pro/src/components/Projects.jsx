import React from 'react'

const Projects = () => {
  const projects = [
    { title: 'E-Commerce Website', tech: 'React, Node.js, MongoDB', desc: 'Full-stack online shopping platform' },
    { title: 'Portfolio Website', tech: 'React, Bootstrap', desc: 'Personal portfolio with responsive design' },
    { title: 'Task Manager App', tech: 'React, Firebase', desc: 'Real-time task management application' },
    { title: 'Weather App', tech: 'JavaScript, API', desc: 'Weather forecast using OpenWeather API' }
  ]

  return (
    <div className="container mt-5">
      <div className="card rounded-4 shadow p-4">
        <h2 className="text-center mb-4">Projects</h2>
        <div className="row g-3">
          {projects.map((project, index) => (
            <div key={index} className="col-md-6">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">{project.title}</h5>
                  <p className="text-muted small mb-2">{project.tech}</p>
                  <p className="card-text">{project.desc}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default Projects