# ml_deploy
stremlit배포 실습


# streamlit 배포시 필수 사항
- os는 linux이므로, linux에서 인식할 수 있는 path로 변경해야 함.
## 1. 파일 path
base_path = os.path.dirname(file)
model_path = os.path.join(base_path, "models", "iris_model_rfc.pkl")