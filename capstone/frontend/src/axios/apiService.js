import axios from 'axios'
const VUE_APP_API_URL = 'http://localhost:8000'

export class APIService {
  async getUsers () {
    const url = `${VUE_APP_API_URL}/api/getUsers/`
    return await axios.get(url)
  }
}
