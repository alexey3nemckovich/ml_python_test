FROM python:3

COPY requirements.txt /
COPY deviation.json /
COPY *.py /

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "generate_plots.py"]
