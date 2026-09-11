# The Digital Judiciary — single container, zero pip installs.
#
# The image is CPython + this source tree, nothing else. The ONLY external
# dependency at runtime is the AI service (api.anthropic.com), and only when
# DJ_JUDGE_MODE=llm; the default oracle mode makes no network call at all.
#
# Build:  docker build -t digital-judiciary .
# Run:    docker run -p 8080:8080 -v dj-data:/data digital-judiciary
# Conformance (the paper's Table 11, live):
#         docker run --rm digital-judiciary python3 run_conformance.py
# LLM judge:
#         docker run -p 8080:8080 -v dj-data:/data \
#           -e DJ_JUDGE_MODE=llm -e ANTHROPIC_API_KEY=sk-... \
#           digital-judiciary

FROM python:3.12-slim

# openssl: GitHub App JWT signing (optional enterprise path)
RUN apt-get update && apt-get install -y --no-install-recommends openssl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY app/ app/
COPY seed/ seed/
COPY config/ config/
COPY deploy/ deploy/
COPY demo/ demo/
COPY LICENSE NOTICE ARCHITECTURE.md ./
COPY serve.py run_conformance.py ./

# Non-root; /data owned by the runtime user for the SQLite volume.
RUN useradd -r -u 10001 judiciary && mkdir -p /data && chown judiciary /data
USER judiciary

ENV DJ_DB=/data/judiciary.db \
    DJ_JUDGE_MODE=oracle \
    DJ_PORT=8080 \
    PYTHONUNBUFFERED=1

VOLUME /data
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD \
  python3 -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8080/v1/healthz',timeout=2)"

CMD ["python3", "serve.py"]
