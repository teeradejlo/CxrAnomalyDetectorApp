from fastapi import FastAPI, UploadFile, File, Form, Header
from fastapi import status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import torch

from PIL import Image
import io

app = FastAPI()

model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path="./yolov5/runs/train/vin2/weights/best.pt")

origins = [
    "http://localhost:8082",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.post("/detect")
def detect(username: str = Form(...), file: UploadFile = File(...)):
    print(username)
    print(file.content_type)
    if file.content_type.startswith("image/"):
        image = Image.open(io.BytesIO(file.file.read()))
        result = model(image)
        retval = result.pandas().xyxyn[0].values.tolist()
        return {"file": file.filename, "result": retval}
    else:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f'File {file.filename} has unsupported extension type',
        )

# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8081)
