FROM python:3.7.2-slim
RUN mkdir /cal_housing
COPY requirements.txt /cal_housing/
COPY model.pkl /cal_housing/
COPY cal_housing_model.py /cal_housing/
WORKDIR /cal_housing
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","/cal_housing/cal_housing_model.py"]
