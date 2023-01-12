<script setup>
import '../assets/common-classes.css'
import '../assets/common-keyframes.css'
import { ref, computed } from 'vue'
import { axiosFastApi } from '../services/axios.js'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

//data
const imgSrc = ref(null)
const diagnosis = ref([])
const detectionOngoing = ref(false)
const detectionStarted = ref(false)

//computed
const diagnosisText = computed(() => {
	if (diagnosis.value.length > 0) {
		let diseaseDict = {}

		diagnosis.value.forEach((val) => {
			if (val[6] in diseaseDict) {
				diseaseDict[val[6]] += 1
			} else {
				diseaseDict[val[6]] = 1
			}
		})

		let retHTML = "<p><strong>Diagnosis:</strong></p>"

		for (const [key, val] of Object.entries(diseaseDict)) {
			retHTML += `<p>${val} ${val > 1 ? "risks" : "risk"} of ${key} detected.</p>`
		}
		return retHTML
	} else {
		return "<p><strong>Diagnosis:</strong></p><p>No risks detected.</p>"
	}
})

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
		detectionOngoing.value = true
		detectionStarted.value = true

		let formData = new FormData()
		const selectedFile = document.getElementById('detectview-fileInput').files[0]

		if (selectedFile) {
			formData.append("file", selectedFile)
			await axiosFastApi.post('/detect', formData, { headers: { 'Content-Type': 'multipart/form-data' } })
				.then((res) => {
					imgSrc.value = `data:image/${res.data.image_format};base64,${res.data.image_b64}`
					diagnosis.value = res.data.diagnosis
				})
				.catch((e) => {
					console.log(e)
					alert('Some errors occurred. Please try again.')
					detectionStarted.value = false
				})
			detectionOngoing.value = false
		} else {
			alert('Some errors occurred. Please try again.')
		}
	} else {
		alert('Please upload an image...')
	}
}

const reset = () => {
	imgSrc.value = null
	diagnosis.value = []
	detectionOngoing.value = false
	detectionStarted.value = false
}
</script>

<script>
export default {
	name: 'detectview',
}
</script>

<template>
	<div class="detectview-container flexbox-center">
		<div class="detectview-panel-1 d-flex">
			<template v-if="!detectionOngoing">
				<div class="detectview-uploadbox justify-content-center" :class="{ 'flexbox-center': imgSrc == null }">
					<template v-if="imgSrc == null">
						<p style="color: lightgrey; cursor: default;">Upload An Image</p>
					</template>
					<template v-else>
						<img class="img-auto-resize" id="detectview-uploaded-img" :src="imgSrc" />
					</template>
				</div>
				<div v-if="!detectionStarted" class="detectview-btn-panel flexbox-center">
					<form>
						<input type="file" id="detectview-fileInput" style="display:none;" @change="selectFile()" />
						<button class="btn btn-dim green-btn" @click.prevent="uploadFile()">Upload</button>
						<button class="btn btn-dim blue-btn" @click.prevent="detectImage()">Detect</button>
					</form>
				</div>
				<div v-else>
					<div v-html="diagnosisText"></div>
					<div class="detectview-btn-panel flexbox-center" style="margin-top: 20px;">
						<button class="btn btn-dim red-btn" @click="reset()">Back</button>
					</div>
				</div>
			</template>
			<template v-else>
				<PulseLoader :loading="true"></PulseLoader>
			</template>
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
}

.detectview-uploadbox {
	display: flex;
	border: dashed 2px black;
	border-radius: 15px;
	margin-bottom: 20px;
	max-height: 100%;
	max-width: 100%;
	height: 300px;
	width: 450px;
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