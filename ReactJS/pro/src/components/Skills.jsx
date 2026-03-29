import React from 'react'

const Skills = () => {
  const skills = [
    { name: 'HTML/CSS', level: 90 },
    { name: 'JavaScript', level: 85 },
    { name: 'React', level: 80 },
    { name: 'Node.js', level: 75 },
    { name: 'Bootstrap', level: 85 },
    { name: 'MongoDB', level: 70 }
  ]

  return (
    <div className="container mt-5">
      <div className="card rounded-4 shadow p-4">
        <h2 className="text-center mb-4">Skills</h2>
        {skills.map((skill) => (
          <div  className="mb-3">
            <div className="d-flex justify-content-between mb-1">
              <span>{skill.name}</span>
              <span>{skill.level}%</span>
            </div>
            <div className="progress">
              <div 
                className="progress-bar bg-black" 
                style={{width: `${skill.level}%`}}
              ></div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Skills