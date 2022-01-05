<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container">
      <a class="navbar-brand" href="#">Ananas</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'home'}">Home</router-link>
          </li>
        </ul>
        <ul class="navbar-nav mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'login'}">Login</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>