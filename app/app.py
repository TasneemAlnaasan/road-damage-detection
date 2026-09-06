
# Streamlit web app: upload a road image, run our trained YOLO model,
# and display the image with detected damage boxes drawn on it
# تطبيق ويب بسيط: رفع صورة طريق، تشغيل موديلنا المدرّب،
# وعرض الصورة مع صناديق التلف المكتشف مرسومة عليها
import streamlit as st
from ultralytics import YOLO
from PIL import Image

# Load the trained model once when the app starts
# تحميل الموديل المدرّب مرة وحدة لما يبدأ التطبيق
model = YOLO("models/best.pt")

st.title("🛣️ Road Damage Detector | كاشف تلف الطرق")
st.write("Upload a road photo to detect potholes and cracks | ارفع صورة طريق للكشف عن الحفر والشقوق")

uploaded_file = st.file_uploader("Choose an image | اختار صورة", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image | الصورة المرفوعة", use_container_width=True)

    if st.button("Detect Damage | كشف التلف"):
        results = model.predict(image, conf=0.25)
        result_image = results[0].plot()

        st.image(result_image, caption="Detection Result | نتيجة الكشف", use_container_width=True, channels="BGR")