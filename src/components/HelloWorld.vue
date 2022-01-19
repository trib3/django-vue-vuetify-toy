<template>
  <v-container>
    <v-row align-content="center" justify="center">
      <v-col
          justify="center"
          cols="12"
          sm="10"
          md="8"
          lg="8"
      >
        <v-card>
          <v-data-table
              :headers="headers"
              :items="profiles"
          >
            <template v-slot:item.thumbnail="{ item }">
              <v-avatar class="my-1">
                <img :src="item.thumbnail"/>
              </v-avatar>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  /**
   * Datatable component to display a data of profiles to clients
   * */
  name: 'HelloWorld',
  /** Component's state, this is reactive when attributes in data are change the UI is updated to reflect that*/
  data() {
    return {
      headers: [
        {text: '', value: 'thumbnail', width: '5%'},
        {text: 'Name', value: 'name'},
        {text: 'Followers', value: 'followers'},
        {text: 'Likes', value: 'likes'},
        {text: 'Post Count', value: 'post_count'}
      ],
      profiles: []
    }
  },
  /** Vue lifecycle hook, this is called when a component is mounted onto a page*/
  async created() {
    const response = await axios.get('/api/profiles')
    this.profiles = response.data
  },
  // An alternative example would leverage the Vuex state manage patterns and library
  // this removes the need to track the profiles array in the component's data state
  // import { mapState } from 'vuex' // import this at the top
  // computed: mapState({
  //   profiles: state => state.profiles.profiles
  // }),
  // created() {
  //   this.$store.dispatch('profiles/getProfiles')
  // }
}
</script>
