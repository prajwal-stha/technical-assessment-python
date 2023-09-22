<template>
  <div>
    <form ref="profileForm" @submit.prevent="passSubmit">
      <fieldset>
        <label class="col-sm-2 control-label"> Name </label>
        <br />
        <div class="form-group">
          <div class="col-md-4 offset-md-4">
            <input
              required
              v-model="form.name"
              name="name"
              class="form-control"
              type="text"
            />
          </div>
        </div>

        <br />
        <div class="form-group">
          <label class="col-sm-2 control-label"> Gender </label>

          <div class="col-md-4 offset-md-4">
            <select
              required
              class="form-control"
              name="gender"
              v-model="form.gender"
            >
              <option value="M">Male</option>
              <option value="F">Female</option>
              <option value="O">Other</option>
            </select>
          </div>
        </div>

        <br />
        <div class="form-group">
          <label class="col-sm-2 control-label"> Phone </label>

          <div class="col-md-4 offset-md-4">
            <input
              required
              v-model="form.phone"
              name="phone"
              class="form-control"
              type="text"
            />
          </div>
        </div>

        <br />
        <div class="form-group">
          <label class="col-sm-2 control-label"> Email </label>

          <div class="col-md-4 offset-md-4">
            <input
              required
              name="email"
              class="form-control"
              type="email"
              v-model="form.email"
            />
          </div>
        </div>

        <br />
        <div class="form-group">
          <label class="col-sm-2 control-label"> Address </label>

          <div class="col-md-4 offset-md-4">
            <input
              required
              name="address"
              class="form-control"
              type="text"
              v-model="form.address"
            />
          </div>
        </div>

        <br />
        <div class="form-group">
          <label class="col-sm-2 control-label"> Nationality </label>

          <div class="col-md-4 offset-md-4">
            <input
              required
              name="nationality"
              class="form-control"
              type="text"
              v-model="form.nationality"
            />
          </div>
        </div>

        <br />
        <div class="form-group">
          <label class="col-sm-2 control-label"> Date of Birth </label>

          <div class="col-md-4 offset-md-4">
            <input
              required
              name="dob"
              class="form-control"
              type="date"
              v-model="form.dob"
            />
          </div>
        </div>

        <br />
        <div class="form-group">
          <label class="col-sm-2 control-label"> Educational background </label>

          <div class="col-md-4 offset-md-4">
            <input
              required
              name="educational_background"
              class="form-control"
              type="text"
              v-model="form.educational_background"
            />
          </div>
        </div>

        <br />
        <div class="form-group">
          <label class="col-sm-2 control-label"> Preffered contact </label>

          <div class="col-md-4 offset-md-4">
            <select
              class="form-control"
              name="preffered_contact"
              v-model="form.preffered_contact"
            >
              <option value="E">Email</option>

              <option value="P">Phone</option>

              <option value="N">None</option>
            </select>
          </div>
        </div>
        <br />
        <div class="form-actions">
          <input
            required
            type="submit"
            class="btn btn-primary"
            value="Create"
          />
        </div>
      </fieldset>
    </form>
  </div>
</template>

<script>
export default {
  name: "FormVue",
  data: () => ({
    form: {
      name: "",
      gender: "",
      phone: "",
      email: "",
      address: "",
      nationality: "",
      dob: "",
      educational_background: "",
      preffered_contact: "N",
    },
  }),

  methods: {
    passSubmit() {
      this.$emit("submitProfile", this.form);
      this.$refs.profileForm.reset();
    },
  },
};
</script>

<style></style>
