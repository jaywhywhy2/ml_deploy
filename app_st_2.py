import streamlit as st
import numpy as np
import pickle
import os

base_path = os.path.dirname(__file__)

#실행  streamlit run app_st_2.py

#모델 로드 함수
@st.cache_resource # 자원 캐싱 기능
def load_model() :
    model_path = os.path.join(base_path, "models", "iris_model_rfc.pkl") 
    # with open ('models/iris_model_lr.pkl','rb') as f :
    with open (model_path,'rb') as f :
                model = pickle.load(f)
    return model
model = load_model()


# # 클래스별 이미지 경로 설정
# def get_image_path(prediction):
#     if prediction == 0:
#         return 'static/setosa.jpg'
#     elif prediction == 1:
#         return 'static/versicolor.jpg'
#     else:
#         return 'static/virginica.jpg'

# 클래스별 이미지 경로 설정
def get_image_path(prediction):
    if prediction == 0:
        return os.path.join(base_path,'static','setosa.jpg')
    elif prediction == 1:
        return os.path.join(base_path,'static','versicolor.jpg')
    else:
        return os.path.join(base_path, 'static','virginica.jpg')


# Streamlit 앱 구성
st.title("Iris 품종 예측")
st.write("꽃받침 길이 , 너비 , 꽃잎 길이 , 너비를 입력하여 품종을 예측해보세요")

# 사용자 입력 받기
sepal_length = st.number_input("꽃받침 길이 (cm)", min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.number_input("꽃받침 너비 (cm)", min_value=0.0, max_value=10.0, value=3.0)
petal_length = st.number_input("꽃잎 길이 (cm)", min_value=0.0, max_value=10.0, value=4.0)
petal_width = st.number_input("꽃잎 너비 (cm)", min_value=0.0, max_value=10.0, value=1.0)

# 예측 버튼
if st.button("예측하기"):
    # 예측 버튼 눌렀을 때
    btn_clicked = True
else:
    btn_clicked = False


if  btn_clicked == True :
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    
    # 모델을 사용하여 예측
    prediction = model.predict(input_data)
    predicted_class = prediction[0]
    
    # 예측된 클래스 이름
    class_name = ['Setosa', 'Versicolor', 'Virginica'][predicted_class]
    # st.subheader(f"예측된 품종: {class_name}")
    
    # # 해당 품종 이미지 표시
    # image_path = get_image_path(predicted_class)
    # st.image(image_path, caption=class_name)

    # 이미지 크기 고정
    col1, col2, col3 = st.columns([1,5,1])
    with col2:
        st.subheader(f"예측된 품종: {class_name}")
        # 해당 품종 이미지 표시
        image_path = get_image_path(predicted_class)
        st.image(image_path, caption=class_name)

else : 
    st.write("값을 입력하고 '예측하기' 버튼을 눌러 결과를 확인하세요.")

