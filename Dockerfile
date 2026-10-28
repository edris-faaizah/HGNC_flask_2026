FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","-m","hgnc_gene_data_collector.app"]
# had to add "-m" because my app.py is in another folder, so we access it as a module, so that it
#doesnt affect my code.