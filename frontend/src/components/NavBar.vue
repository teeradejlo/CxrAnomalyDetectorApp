<script>
export default {
	name: 'navbar',
}
</script>

<template>
	<nav>
		<div class="navbar-nav-head">teeradejlo</div>
		<div class="navbar-link-list">
			<div class="navbar-nav-link">Home</div>
			<div class="navbar-nav-link navbar-last-nav-link">Detect</div>
		</div>
	</nav>
</template>

<style scoped>
nav {
	display: flex;
	background-color: rgb(206, 255, 216);
	padding: 20px;
	box-shadow: 0 1px 20px rgb(181, 181, 181);
}

.navbar-link-list {
	display: flex;
	margin-top: -1.5px;
}

.navbar-nav-head {
	font-size: 20px;
	font-weight: 800;
	margin-left: 10px;
	margin-right: 40px;
}

.navbar-nav-head:hover {
	cursor: default;
}

.navbar-nav-link {
	position: relative;
	transition: background-color 0.2s;
	padding: 5px 20px;
	border-radius: 5px;
	font-weight: 200;
}

.navbar-nav-link:after {
	content: "";
	background: black;
	position: absolute;
	bottom: 15%;
	right: 0;
	height: 70%;
	width: 1px;
}

.navbar-nav-link:hover {
	cursor: pointer;
	color: white;
	background-color: rgb(69, 127, 82);
}

.navbar-last-nav-link:after {
	width: 0px;
}
</style>

