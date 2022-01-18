import api from '@/services/api'

export default {
  fetchAmbassadors() {
    return api.get(`ambassadors/`)
              .then(response => response.data)
  },
}