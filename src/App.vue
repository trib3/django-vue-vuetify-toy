<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
    Toy Problem
    </v-app-bar>
    <v-main>
      <v-content>
        <HelloWorld/>
      </v-content>
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from "@/components/HelloWorld";

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
