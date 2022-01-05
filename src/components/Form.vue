<template>
  <form>
    <div class="row">
      <div class="col-lg-6 offset-lg-3 col-xl-4 offset-xl-4">
        <div class="card border-primary">
          <div class="card-header bg-primary text-white">{{ title }}</div>
          <div class="card-body">
            <slot></slot>

            <div class="text-center">
              <button type="submit" class="btn btn-primary">{{ get_button_title }}</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import {defineComponent} from "vue";

export default defineComponent({
  props: {
    title: String,
    button_title: String
  },
  computed: {
    get_button_title() {
      return this.button_title || this.title
    }
  }
})
</script>