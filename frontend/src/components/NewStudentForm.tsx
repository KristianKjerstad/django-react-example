import { useState } from 'react'
// eslint-disable-next-line @typescript-eslint/no-unused-vars
import axios, { AxiosResponse } from 'axios'
import { API_URL } from '../constants'

export type Student = {
  pk: number
  name: string
  email: string
  document: string
  phone: string
}

const NewStudentForm = () => {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [document, setDocument] = useState('')
  const [phone, setPhone] = useState('')
  const [error, setError] = useState('')

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    setError('')
    try {
      const response: AxiosResponse<Student> = await axios.post(
        `${API_URL}/students/`,
        {
          name,
          email,
          document,
          phone,
        }
      )

      console.log(response.data)
    } catch (error) {
      if (axios.isAxiosError(error)) {
        setError(error.message)
      } else {
        console.error(error)
      }
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <div style={{ display: 'flex', flexDirection: 'column' }}>
        <div style={{ marginBottom: '10px' }}>
          <label>
            Name:
            <input
              type="text"
              value={name}
              onChange={(event) => setName(event.target.value)}
            />
          </label>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>
            Email:
            <input
              type="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
            />
          </label>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>
            Document:
            <input
              type="text"
              value={document}
              onChange={(event) => setDocument(event.target.value)}
            />
          </label>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>
            Phone:
            <input
              type="text"
              value={phone}
              onChange={(event) => setPhone(event.target.value)}
            />
          </label>
        </div>
      </div>
      <button type="submit">Create Student</button>
      {error && <p>{error}</p>}
    </form>
  )
}

export default NewStudentForm
