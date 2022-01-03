<template>
  <div class="profile">
    <h1>Create Profile !</h1>
    <p v-if="getResponse">{{ getResponse }}</p>
    <form-vue @submitProfile="submit"></form-vue>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import FormVue from "../components/Form.vue";

export default {
  computed: {
    ...mapGetters(["getResponse"]),
  },
  methods: {
    ...mapActions(["createProfile"]),

    submit(data) {
      this.createProfile(data);
    },
  },
  components: {
    FormVue,
  },
};
</script>
