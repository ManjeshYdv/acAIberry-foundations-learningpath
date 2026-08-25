# Phase 5: PM2, Docker, and Azure

**Days 41–50 · Result:** you can keep the API running, package it as a container, explain its Azure resources, connect to a VM with SSH, and run the same container remotely.

Keep the service small. PM2 teaches process management first; Docker then replaces machine-specific setup with a repeatable image. Do not run PM2 inside the container.

## Day 41: Run the API as a Linux process

**Goal:** Connect an application command to its process, port, environment, and log.

**Commands:** `uv run uvicorn`, `&`, `ps`, `pgrep -af`, `ss -lntp`, `kill`, `tail -f`.

**Task:** Start the API on port `8000` with output redirected to a log. Find its PID and listening port, call `/health`, follow the log, and stop it normally.

**Done when:** `notes/api-process.md` maps command → PID → port → log → HTTP response.

**Resource:** [Uvicorn repository and usage](https://github.com/encode/uvicorn)

## Day 42: Keep the API running with PM2

**Goal:** Use a process manager to start, inspect, restart, and log a long-running command.

**Commands:** `pm2 start`, `pm2 list`, `pm2 show`, `pm2 logs`, `pm2 restart`, `pm2 stop`, `pm2 delete`.

**Task:** Install PM2 from its official guide, then manage the `uv run uvicorn ...` command as `ticket-api`. Stop it, restart it, read its logs, and inspect its PID and restart count.

**Done when:** PM2 reports the process online, `/health` works, logs are readable, and you can explain that PM2 manages a process but does not create a container.

**Resource:** [PM2 quick start](https://pm2.keymetrics.io/docs/usage/quick-start/)

## Day 43: Understand images and containers

**Goal:** Distinguish a Dockerfile, image, container, registry, port, and volume.

**Commands:** `docker version`, `docker run --rm hello-world`, `docker image ls`, `docker ps`, `docker ps -a`.

**Task:** Run `hello-world`, inspect the downloaded image and stopped container state, then remove only the disposable stopped container if one remains.

**Done when:** Draw the path Dockerfile → image → running container and explain why deleting a container does not delete its image.

**Resource:** [Docker: what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)

## Day 44: Write a small Dockerfile

**Goal:** Describe the exact environment and command required to run the API.

**Commands:** Dockerfile `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`; `.dockerignore`.

**Task:** Write a Dockerfile based on a slim supported Python image. Install dependencies from the `uv` lockfile, copy only needed code and synthetic data, train the model during the build, switch to a non-root user, and start Uvicorn. Exclude `.git`, `.env`, `.venv`, logs, caches, and private keys from the build context.

**Done when:** You can explain each layer and `docker build -t ticket-api:local .` succeeds without copying secrets.

**Resources:** [Dockerfile overview](https://docs.docker.com/build/concepts/dockerfile/) · [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/)

## Day 45: Build, run, inspect, and log a container

**Goal:** Operate the application inside its container boundary.

**Commands:** `docker build`, `docker run`, `docker logs`, `docker exec`, `docker inspect`, `docker stats`, `docker stop`.

**Task:** Run the image as `ticket-api` with host port `8000` mapped to container port `8000`. Call `/health` and `/predict`, view logs, inspect its environment and port mapping without printing secrets, check resource use, and stop it gracefully.

**Done when:** The container is removed/recreated without changing the image, and the API behaves the same each time.

**Resource:** [Docker container command reference](https://docs.docker.com/reference/cli/docker/container/)

## Day 46: Manage the app with Docker Compose

**Goal:** Save container configuration as a small, repeatable YAML file.

**Commands:** `docker compose config`, `docker compose up -d`, `docker compose ps`, `docker compose logs`, `docker compose down`.

**Task:** Create `compose.yaml` for the API. Add a health check, environment-file reference, loopback-only port mapping, and `restart: unless-stopped`. Keep it to one service until the project truly needs another.

**Done when:** A new shell can start, inspect, test, and stop the app using only documented Compose commands.

**Resource:** [Docker Compose quickstart](https://docs.docker.com/compose/gettingstarted/)

## Day 47: Understand Azure resources and cost

**Goal:** Know what will be created before spending money.

**Commands/tools:** Azure Portal or `az login`, `az account show`, `az group list`, `az resource list`.

**Task:** Draw this resource map: subscription → resource group → virtual network/subnet → network interface → VM → OS disk, plus public IP and network security group. Choose one region and a small Ubuntu VM size, review its current price, and configure a budget alert before creation.

**Done when:** `notes/azure-plan.md` lists each resource, purpose, region, estimated cost, allowed inbound traffic, and the resource-group deletion plan.

**Resources:** [Azure fundamental concepts](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/considerations/fundamental-concepts) · [Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/)

## Day 48: Create a small Azure VM

**Goal:** Create one minimal VM with key-based SSH and understand every generated resource.

**Commands/tools:** Azure Portal or the [Azure CLI VM quickstart](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli); `az vm show`, `az resource list`.

**Task:** Create a dedicated resource group and small Ubuntu VM using the practice public SSH key. Restrict inbound SSH to your current public IP. Do not enable password login or expose the application port yet.

**Done when:** Save resource names and the VM public IP—not secret material—in `notes/azure-vm.md`, and compare the resource list with Day 47's diagram.

**Resource:** [Azure Linux VM overview](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/overview)

## Day 49: Inspect and prepare the VM over SSH

**Goal:** Treat the VM as another Linux machine and reuse the earlier diagnostic commands.

**Commands:** `ssh -i`, `scp`, `uname -a`, `uptime`, `htop`, `free -h`, `df -h`, `ss -lntp`, `systemctl`, `journalctl`.

**Task:** Connect as the non-root VM user. Copy one harmless note to `/tmp` with `scp`, then inspect CPU, memory, disk, processes, ports, and services. Update approved packages, install Docker from current official instructions, and clone the project rather than copying secrets.

**Done when:** `notes/vm-baseline.md` records the VM facts and shows that Docker runs. Disconnect and reconnect successfully using the same key.

**Resources:** [Azure SSH guidance](https://learn.microsoft.com/en-us/azure/virtual-machines/linux-vm-connect) · [Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

## Day 50: Checkpoint deploy the container to Azure

**Goal:** Run the same Compose-defined application on the VM and verify it over SSH.

**Commands:** `git clone` or `git pull --ff-only`, `docker compose up -d`, `docker compose ps`, `docker compose logs`, `ssh -L`.

**Task:** Deploy the project on the VM, build/start it with Compose, and bind the published API port to the VM's loopback interface. From your machine, create an SSH tunnel to port `8000`, then call `/health` and `/predict`. Reboot the VM and verify the restart policy.

**Done when:** The API works through the tunnel, the application is not directly exposed to the internet, logs show the request, and `notes/azure-deploy.md` contains the repeatable commands.

**Resource:** [OpenSSH port forwarding](https://www.ssh.com/academy/ssh/tunneling-example)

### Phase checkpoint

Starting with only the VM IP and SSH key path, connect, check resources with `htop`/`free`/`df`, inspect containers and logs, reach the API through a tunnel, and explain every Azure resource supporting it.
