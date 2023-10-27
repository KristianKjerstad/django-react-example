import axios from 'axios'
import type { Ingredient, Recipe } from './types'

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

export const getAllIngredients = async (): Promise<Ingredient[]> => {
  return axios
    .get(`${API_BASE_URL}/cocktailRecipes/ingredients`)
    .then((response) => {
      return response.data
    })
    .catch((error) => {
      console.error('an error occurred while fetching ingredients', error)
    })
}

export const getFilteredRecipes = async (ingredients: Ingredient[]): Promise<Recipe[]> => {
  const ingredient_ids = ingredients.map((ingredient) => ingredient.id)
  const ingredient_ids_as_string = ingredient_ids.join(',')
  return axios
    .get(`${API_BASE_URL}/cocktailRecipes/filtered/?values=${ingredient_ids_as_string}`)
    .then((response) => {
      return response.data
    })
    .catch((error) => {
      console.error('an error occurred while fetching recipes', error)
    })
}
