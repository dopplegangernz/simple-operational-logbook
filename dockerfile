FROM python:3

WORKDIR /app

COPY . .

RUN make install

EXPOSE 5000

CMD ["make", "run"]
