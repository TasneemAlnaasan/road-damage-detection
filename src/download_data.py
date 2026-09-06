import os
from dotenv import load_dotenv
from roboflow import Roboflow

load_dotenv()

rf = Roboflow(api_key=os.getenv("ROBOFLOW_API_KEY"))
project = rf.workspace("roaddamage-msfnj").project("road-damage-ww8ex")
version = project.version(1)
dataset = version.download("yolov8")
