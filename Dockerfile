FROM python:3.11-alpine AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-alpine

WORKDIR /app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --from=builder /root/.local /home/appuser/.local
COPY app/ ./app/

ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser

EXPOSE 5000

CMD ["python", "app/app.py"]
