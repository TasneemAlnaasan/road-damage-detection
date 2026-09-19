# 🛣️ Road Damage Detection

🔗 **[Live Demo](https://pzhxtgoklzzt6ftujeusmv.streamlit.app/)**

A computer vision project that detects and classifies road surface damage
(potholes and cracks) from images, using a fine-tuned YOLOv8 model.


## Problem

Manually surveying roads for damage is slow and inconsistent. This project
explores whether a lightweight object detection model can automatically flag
damage from a simple photo — a step toward faster, more consistent road
maintenance prioritization.

## Detected Damage Types

- Pothole
- Alligator cracking
- Longitudinal cracking
- Lateral cracking

## Dataset

3,321 labeled road images (train/valid/test split: 2325/664/332), sourced from
[Road Damage Dataset on Roboflow Universe](https://universe.roboflow.com/roaddamage-msfnj/road-damage-ww8ex) (CC BY 4.0).

## Model & Results

Fine-tuned YOLOv8n (transfer learning from COCO pretrained weights), trained
for 50 epochs on Google Colab (free T4 GPU).

| Class | mAP50 |
|---|---|
| Alligator cracking | 0.64 |
| Longitudinal cracking | 0.60 |
| Pothole | 0.61 |
| Lateral cracking | 0.37 |
| **Overall** | **0.55** |

**Known limitation:** the model performs noticeably worse on lateral cracking,
likely due to visual similarity with longitudinal cracks. This is a clear
target for future improvement (more data / longer training).

## Demo

🔗 Try the live app here: (https://pzhxtgoklzzt6ftujeusmv.streamlit.app/)

## Tech Stack

- YOLOv8 (Ultralytics)
- OpenCV
- Streamlit
- Google Colab (training)
- Roboflow (dataset)

## How to Run Locally

\`\`\`bash
git clone <https://github.com/TasneemAlnaasan/road-damage-detection.git>
cd road-damage-detection
pip install -r requirements.txt
cd app
streamlit run app.py
\`\`\`

## Future Improvements

- Expand training data (more images per class, especially lateral cracking)
- Manual annotation of locally-collected images
- Deploy as a public API alongside the Streamlit interface
