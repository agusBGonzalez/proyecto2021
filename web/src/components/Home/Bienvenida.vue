<template>
  <div class="container text-center mb-5">
    <h1 class="display-1 bienvenida">¡Bienvenidos a EvacuAR!</h1>
  </div>
</template>

<script>
export default {
  name: "Bienvenida",
};
</script>

<style scoped>
.bienvenida {
  font-weight: 900;

  user-select: none;
  -webkit-touch-callout: none; 

  background-image: linear-gradient(
    90deg,
    rgba(214, 30, 178, 1) 0%,
    rgba(255, 231, 26, 1) 50%,
    rgba(0, 200, 255, 1) 100%
  );
  background-clip: text;
  color: transparent;
  background-size: 400%;
  animation: bg-animation 5s infinite alternate;
}

@keyframes bg-animation {
  0% {
    background-position: left;
  }
  100% {
    background-position: right;
  }
}
</style>