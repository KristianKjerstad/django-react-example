import axios from 'axios'
import type { Recipe } from './types'

const API_BASE_URL = 'http://localhost:8000'

export const getAllRecipes = async (): Promise<Recipe[]> => {
  return axios
    .get(`${API_BASE_URL}/cocktailRecipes/`)
    .then((response) => {
      return response.data
    })
    .catch((error) => {
      console.error('an error occurred while fetching recipes', error)
    })
}
