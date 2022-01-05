<script>
import {defineComponent, h} from "vue";

export default defineComponent({
  props: {
    label: String,
    attribute: String,
    errors: Object
  },
  render() {
    let children = [
      h("label", {class: "form-label"}, this.label),
      this.$slots.default().map(item => {
        return h(item, {
          class: {
            "is-invalid": this.errors !== null && typeof [this.attribute] != 'undefined',
            "is-valid": this.errors !== null && typeof this.errors[this.attribute] == 'undefined'
          }
        })
      })
    ]

    if (this.errors !== null && typeof this.errors[this.attribute] != 'undefined' &&
        Array.isArray(this.errors[this.attribute])) {
      this.errors[this.attribute].forEach(item => {
        children.push(h("div", {class: "invalid-feedback"}, item))
      })
    }

    return h("div", {class: "mb-3"}, children)
  }
})
</script>