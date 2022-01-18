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
              :items="ambassadors"
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
import {mapState} from 'vuex'

export default {
  name: 'HelloWorld',
  data() {
    return {
      headers: [
        {text: '', value: 'thumbnail', width: '5%'},
        {text: 'Name', value: 'name'},
        {text: 'EMV', value: 'emv'},
        {text: 'Post Count', value: 'post_count'}
      ],
      ambassadors2: []
    }
  },
  computed: mapState({
    ambassadors: state => state.ambassadors.ambassadors
  }),
  created() {
    this.$store.dispatch('ambassadors/getAmbassadors')
  }
}
</script>
