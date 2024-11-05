FROM fedora:40 AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN --mount=target=/src uv build --project /src --out-dir /dist

FROM quay.io/jumpstarter-dev/jumpstarter:latest
RUN --mount=from=builder,source=/dist,target=/dist \
  VIRTUAL_ENV=/jumpstarter uv pip install /dist/*.whl
