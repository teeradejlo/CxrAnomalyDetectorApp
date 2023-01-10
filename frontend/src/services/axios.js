import axios from "axios"

const axiosFastApi = axios.create({
	baseURL: "http://localhost:8081/api",
})

export { axiosFastApi };