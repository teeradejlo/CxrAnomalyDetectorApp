<script setup>
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
</script>

<template>
	<div class="app-container">
		<NavBar />
		<RouterView />
	</div>
</template>

<style scoped>
.app-container {
	display: flex;
	flex-direction: column;
	height: 100vh;
}
</style>
