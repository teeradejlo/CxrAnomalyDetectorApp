<script setup>
import '../assets/common-classes.css'
import '../assets/common-keyframes.css'
import { ref } from 'vue'
import { axiosFastApi } from '../services/axios.js'

//data
const imgSrc = ref(null)
const detectionDone = ref(false)
const detectionStart = ref(false)

//methods
const uploadFile = () => {
	document.getElementById('detectview-fileInput').click()
}

const selectFile = () => {
	const selectedFile = document.getElementById('detectview-fileInput').files[0]
	let pattern = /image-*/

	if (!selectedFile.type.match(pattern)) {
		alert('Please upload an image...')
		return
	}

	const reader = new FileReader()

	reader.addEventListener("load", () => {
		// convert image file to base64 string
		imgSrc.value = reader.result
	}, false)

	reader.readAsDataURL(selectedFile)
}

const detectImage = async () => {
	if (imgSrc.value != null) {
		imgSrc.value = null
		detectionStart.value = true;

		let formData = new FormData();
		const selectedFile = document.getElementById('detectview-fileInput').files[0]

		if (selectedFile) {
			formData.append("file", selectedFile);
			await axiosFastApi.post('/detect', formData, { headers: { 'Content-Type': 'multipart/form-data' } })
				.then((res) => {
					imgSrc.value = `data:image/${res.data.image_format};base64,${res.data.image_b64}`
				})
				.catch((e) => {
					console.log(e)
				})
		} else {
			alert('Some errors occurred. Please try again.')
		}
	} else {
		alert('Please upload an image...')
	}
}
</script>

<script>
export default {
	name: 'detectview',
}
</script>

<template>
	<div class="detectview-container flexbox-center">
		<div v-if="!detectionStart" class="detectview-panel-1 d-flex">
			<div class="detectview-uploadbox justify-content-center" :class="{ 'flexbox-center': imgSrc == null }">
				<template v-if="imgSrc == null">
					<p style="color: lightgrey; cursor: default;">Upload An Image</p>
				</template>
				<template v-else>
					<img class="img-auto-resize" id="detectview-uploaded-img" v-bind:src="imgSrc" />
				</template>
			</div>
			<div class="detectview-btn-panel flexbox-center">
				<form>
					<input type="file" id="detectview-fileInput" style="display:none;" @change="selectFile()" />
					<button class="btn btn-dim green-btn" @click.prevent="uploadFile()">Upload</button>
					<button class="btn btn-dim blue-btn" @click.prevent="detectImage()">Detect</button>
				</form>
			</div>
		</div>
		<div v-else class="detectview-panel-1 d-flex">
			<div class="detectview-uploadbox justify-content-center" :class="{ 'flexbox-center': imgSrc == null }">
				<img class="img-auto-resize" v-bind:src="imgSrc" />
			</div>
		</div>
	</div>
</template>

<style scoped>
.detectview-container {
	flex-grow: 1;
	overflow: hidden;
	background-color: white;
	animation: fade-in 0.5s ease 0s 1 normal backwards, translate-in-top 0.5s ease 0s 1 normal backwards;
}

.detectview-panel-1 {
	background-color: white;
	border-radius: 25px;
	box-shadow: 0 0 50px rgb(221, 221, 221);
	flex-direction: column;
	padding: 30px;
	max-width: 80%;
	max-height: 80%;
	width: 550px;
}

.detectview-uploadbox {
	display: flex;
	border: dashed 2px black;
	border-radius: 15px;
	margin-bottom: 30px;
	height: 350px;
	width: 100%;
}

.detectview-btn-panel button {
	margin: 0 20px;
}

.detectview-btn-panel button:first-child {
	margin-left: 0;
}

.detectview-btn-panel button:last-child {
	margin-right: 0;
}
</style>