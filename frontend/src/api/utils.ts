import axios, { AxiosError, AxiosResponse } from 'axios'
import { API_URL } from '../constants'
import { Student } from '../components/NewStudentForm'

export const getAllStudents = async (): Promise<Student[]> => {
  axios
    .get(`${API_URL}/students`)
    .then((response: AxiosResponse<Student>) => {
      console.log('got', response.data)
      return response.data
    })
    .catch((error: AxiosError) => {
      console.error(error)
    })
}
