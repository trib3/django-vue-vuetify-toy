<template>
  <div class="hello">
    <img src='@/assets/logo-django.png' style="width: 250px" />
    <p>The data below is added/removed from the SQLite Database using Django's ORM and Rest Framework.</p>
    <br/>
    <p>Subject</p>
    <input type="text" placeholder="Hello" v-model="subject">
    <p>Message</p>
    <input type="text" placeholder="From the other side" v-model="msgBody">
    <br><br>
    <input 
      type="submit" 
      value="Add" 
      @click="addMessage({ subject: subject, body: msgBody })" 
      :disabled="!subject || !msgBody">

    <hr/>
    <h3>Messages on Database</h3>
    <p v-if="messages.length === 0">No Messages</p>
    <div class="msg" v-for="(msg, index) in messages" :key="index">
        <p class="msg-index">[{{index}}]</p>
        <p class="msg-subject" v-html="msg.subject"></p>
        <p class="msg-body" v-html="msg.body"></p>
        <input type="submit" @click="deleteMessage(msg.pk)" value="Delete" />
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: "Messages",
  computed: mapState({
    ambassadors: state => state.ambassadors.ambassadors
  }),
  created() {
    this.$store.dispatch('ambassadors/getAmbassadors')
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
