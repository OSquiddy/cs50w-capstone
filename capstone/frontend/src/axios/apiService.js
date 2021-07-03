import axios from 'axios'
const API_URL = 'http://localhost:8000'

export class APIService {
  async getUsers () {
    const url = `${API_URL}/api/getUsers/`
    return await axios.get(url)
  }
}
