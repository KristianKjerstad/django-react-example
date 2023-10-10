import { useEffect, useState } from 'react'
import { Student } from './NewStudentForm'
import { API_URL } from '../constants'
import axios, { AxiosError, AxiosResponse } from 'axios'

const Header = () => {
  const [students, setStudents] = useState<Student[]>()

  useEffect(() => {
    axios
      .get(`${API_URL}/students`)
      .then((response: AxiosResponse<Student>) => {
        setStudents(response.data)
      })
      .catch((error: AxiosError) => {
        console.error(error)
      })
  }, [])

  return (
    <div className="text-center">
      <img
        src="https://blog.logrocket.com/wp-content/uploads/2022/09/logrocket-logo-frontend-analytics.png"
        width="300"
        className="img-thumbnail"
        style={{ marginTop: '20px' }}
      />
      <hr />
      <h5>
        <i>presents</i>
      </h5>
      <h1>App with React + Django</h1>
      <h2>List of students found:</h2>
      {students &&
        students.map((student) => {
          return <p>{student.name}</p>
        })}
    </div>
  )
}

export default Header
