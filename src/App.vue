<template>
  <Navbar />
  <div class="container mt-3">
    <router-view />
  </div>
</template>

<style>

</style>
<script>
import Navbar from "@/components/Navbar";
export default {
  components: {Navbar}
}
</script>