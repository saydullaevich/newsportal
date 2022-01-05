<template>
  <Form title="Tizimga kirish" @submit.stop.prevent="onLogin">
    <FormGroup label="Login" :errors="errors" attribute="Username">
      <input type="text" class="form-control" v-model="form.username" />
    </FormGroup>
    <FormGroup label="Parol" :errors="errors" attribute="Password">
      <input type="password" class="form-control" v-model="form.password" />
    </FormGroup>
  </Form>

  {{ errors }}
</template>
<script>
import Form from "@/components/Form";
import FormGroup from "@/components/FormGroup";
export default {
  components: {FormGroup, Form},
  data() {
    return {
      form: {
        username: "",
        password: ""
      },
      errors: null
    }
  },
  methods: {
    async onLogin() {
      this.errors = {}
      let resp = await this.$axios.post('account/login/', this.form)
      if (resp.success) {
        alert(JSON.stringify(resp))
      } else if (resp.fail) {
        this.errors = resp.data
      }
    }
  }
}
</script>