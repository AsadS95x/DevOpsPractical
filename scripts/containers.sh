docker system prune --all --volumes --force
docker compose build --parallel && docker compose push