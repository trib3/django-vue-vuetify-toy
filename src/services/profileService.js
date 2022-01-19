import api from '@/services/api'

export default {
  fetchProfiles() {
    return api.get(`profiles/`)
              .then(response => response.data)
  },
}