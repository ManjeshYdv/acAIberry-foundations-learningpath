# Day 17: Inspect a Service

**Date:** Wed Sep 23, 2026
**Time spent:** 1:00 PM to 2:00 PM

## Service inspected

**Service:** docker

Active/State : Active: active (running) since Wed 2026-09-23 10:10:13 +0545; 3h 59min ago
Main PID: 3529 (dockerd)

**five log Lines here**
Sep 23 10:10:12 acaiberry dockerd[3529]: time="2026-09-23T10:10:12.763432927+05:45" level=info msg="Initializing buildkit"
Sep 23 10:10:13 acaiberry dockerd[3529]: time="2026-09-23T10:10:13.165333464+05:45" level=info msg="Completed buildkit initialization"
Sep 23 10:10:13 acaiberry dockerd[3529]: time="2026-09-23T10:10:13.167581021+05:45" level=info msg="Daemon has completed initialization"
Sep 23 10:10:13 acaiberry dockerd[3529]: time="2026-09-23T10:10:13.167597972+05:45" level=info msg="API listen on /run/docker.sock"
Sep 23 10:10:13 acaiberry systemd[1]: Started docker.service - Docker Application Container Engine.

## Commands used

```bash
systemctl status docker
systemctl list-units --type=service
journalctl -u docker --since today
journalctl -u docker --since today -n 5
