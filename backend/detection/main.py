from fastapi import FastAPI, UploadFile, File, Form, Header, Response
from fastapi import status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import torch
import base64

from PIL import Image
import io

app = FastAPI()

model = torch.hub.load(
    "ultralytics/yolov5", "custom", path="./yolov5/runs/train/vin2/weights/best.pt"
)

origins = [
    "http://localhost:8082",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/api/detect")
def detect(file: UploadFile = File(...)):
    print(file.content_type)
    if file.content_type.startswith("image/"):
        image = Image.open(io.BytesIO(file.file.read()))
        result = model(image)
        retval = result.pandas().xyxyn[0].values.tolist()
        retImg = result.render()
        retImg = [Image.fromarray(arr) for arr in retImg]
        img_byte_arr = io.BytesIO()
        retImg[0].save(img_byte_arr, format="PNG")
        img_byte_arr = img_byte_arr.getvalue()
        retImg = base64.b64encode(img_byte_arr)
        return {"diagnosis": retval, "image_b64": retImg, "image_format": "png"}
    else:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"File {file.filename} has unsupported extension type",
        )


# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8081)
