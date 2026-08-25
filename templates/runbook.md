# Ticket Classifier Runbook

## Connect

- VM/resource name:
- SSH command with placeholders only:
- Expected Azure resource group:

## Check the host

```text
uptime
free -h
df -h
htop
ss -lntp
```

## Check the app

```text
docker compose ps
docker compose logs --since 10m
curl --fail http://127.0.0.1:8000/health
```

## Deploy

List the exact commands to pull and start a known image. Record the expected tag/digest without credentials.

## Roll back

List the previous known image and commands to restore it, then repeat the health check.

## Common failures

| Symptom | First check | Next evidence |
| --- | --- | --- |
| SSH fails | NSG rule and current IP | SSH verbose output |
| Health fails | `docker compose ps` | Container logs |
| Connection refused | `ss -lntp` | Port mapping |
| Container restarts | Container logs | Memory/disk/config |
| Prediction fails | Application log | Model path and artifact |

## Cleanup

Document how to remove unused containers/images and, when finished, delete the Azure resource group to stop charges.
