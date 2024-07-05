import streamlit as st

st.title("Pothole Detection using Darknet YOLO v2")
st.link_button("Project Github","https://github.com/pkcktkksh98/Pothole_Detection")
st.text(
    " This project is for detecting a pothole and would be a great asset for city \n municiple to have this model. The accuracy might not be that good yet,\n but with some extra dataset, we can improve the accuracy of the model.\n In addition, we might be able to improve the system\n by obtaining the location of the pothole that was detected.")
st.header("Loss & mAP Graph")
st.image("nn/data/pothole_voc/chart_potholes.png")
st.header("Image Inferencing")
st.image("nn/data/predictions1.jpg")
st.image("nn/data/predictions2.jpg")
st.header("Video Inferencing")
st.video("nn/data/video.webm")