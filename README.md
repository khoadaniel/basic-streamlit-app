# hate-speech-detection-streamlit-app



docker run -p 8000:8000 helloworld-backend
docker run -p 8001:8001 helloworld-frontend

## run streamlit app
streamlit run ./app/streamlit_app.py --server.port=8001 --server.address=0.0.0.0

## run uvicorn fastapi app
python -m uvicorn fastapi_app:app --host 0.0.0.0 --port 8000


## Ref:
https://www.youtube.com/watch?v=HG6yIjZapSA


https://blog.jcharistech.com/2022/08/05/deploying-streamlit-and-fastapi-apps-using-docker-and-docker-compose/