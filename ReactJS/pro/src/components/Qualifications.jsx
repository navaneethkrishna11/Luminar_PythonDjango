import React from 'react'

const Qualifications = () => {
  return (
    <div className="container mt-5">
      <div className="card rounded-4 shadow p-4">
        <h2 className="text-center mb-4">Qualifications</h2>
        
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-dark">
              <tr>
                <th>Degree</th>
                <th>Institution</th>
                <th>Year</th>
                <th>Percentage/CGPA</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Bachelor of Science (B.Sc)</td>
                <td>University of Technology</td>
                <td>2015 - 2018</td>
                <td>8.5 CGPA</td>
              </tr>
              <tr>
                <td>Higher Secondary (12th)</td>
                <td>St. Mary's High School</td>
                <td>2014 - 2015</td>
                <td>85%</td>
              </tr>
              <tr>
                <td>Secondary (10th)</td>
                <td>St. Mary's High School</td>
                <td>2012 - 2013</td>
                <td>88%</td>
              </tr>
              <tr>
                <td>Master of Computer Applications (MCA)</td>
                <td>Institute of Technology</td>
                <td>2018 - 2020</td>
                <td>9.0 CGPA</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}

export default Qualifications