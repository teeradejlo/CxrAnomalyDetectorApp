<script setup>
import '../assets/common-classes.css'
import '../assets/common-keyframes.css'
</script>

<script>
export default {
	name: 'homeview',
}
</script>

<template>
	<div class="homeview-container flexbox-center">
		<div class="homeview-panel-1 flexbox-center">
			<div>
				<h1 data-text="Chest X-Ray">Chest X-Ray</h1>
				<h1 data-text="Anomaly">Anomaly</h1>
				<h1 data-text="Detector">Detector</h1>
				<p>Developed with <a href="https://github.com/ultralytics/yolov5" target="_blank">YOLOv5</a></p>
			</div>
			<div class="homeview-icon"></div>
		</div>
		<div class="homeview-panel-2 flexbox-center">
			<div>
				<button class="btn btn-dim homeview-button" @click="() => this.$router.push('/detect')">
					Try It Now!
				</button>
			</div>
		</div>
	</div>
</template>

<style scoped>
.homeview-container {
	flex-grow: 1;
	flex-direction: column;
	overflow: hidden;
	background-color: white;
}

.homeview-panel-1 {
	width: 100%;
	height: 400px;
	text-align: right;
}

.homeview-panel-1 div:first-child {
	margin-right: 60px;
}

.homeview-panel-1 h1 {
	position: relative;
	line-height: 1.2;
	font-size: 4.5rem;
	margin-top: 0;
	margin-bottom: 0;
	animation: fade-in 0.5s ease 0s 1 normal backwards, translate-in-top 0.5s ease 0s 1 normal backwards;
}

.homeview-panel-1 h1:nth-child(2) {
	animation-delay: 0.25s;
}

.homeview-panel-1 h1:nth-child(3) {
	animation-delay: 0.5s;
}

.homeview-panel-1 h1::after {
	position: absolute;
	content: attr(data-text);
	top: 0;
	right: 0;
	line-height: 0.9em;
	transform-origin: bottom;
	transform: rotateX(180deg);
	background-image: linear-gradient(0deg, #000000 0, transparent 50%);
	background-clip: text;
	-webkit-background-clip: text;
	color: transparent;
	opacity: 0.15;
}

.homeview-panel-1 p {
	text-align: right;
	font-size: 25px;
	font-weight: 200;
	animation: fade-in 0.5s ease 0.75s 1 normal backwards, translate-in-top 0.5s ease 0.75s 1 normal backwards;
}

.homeview-icon {
	aspect-ratio: 1 / 1;
	height: 75%;
	border-radius: 50%;
	box-shadow: 0 0 20px rgb(200, 200, 200);
	background-position: center;
	background-size: 120%;
	animation: fade-in 2s ease 0s 1 normal backwards;
	background-image: url("https://media.istockphoto.com/id/920917304/vector/human-lungs-with-hand-holding-magnifying-glass-medical-tool-for-diagnosing-of-diseases-of.jpg?s=612x612&w=0&k=20&c=JFc0T6dXofa-v28yVPdb2Wymyp6UGezAREE9jfL1Dos=");
}

.homeview-panel-2 {
	margin-bottom: 3%;
}

.homeview-button {
	font-size: 20px;
	padding: 15px 30px;
	color: white;
	background-color: rgb(78, 216, 106);
	animation: fade-in 1s ease 0s 1 normal backwards, homeview-translate-in-right 1s ease 0s 1 normal backwards;
}

.homeview-button:active {
	-webkit-transform: translateY(2px);
	transform: translateY(2px);
}

@keyframes homeview-translate-in-right {
	from {
		transform: translateX(40px);
	}

	to {
		transform: translateX(0px);
	}
}
</style>
