# Phase 6: CI/CD and Operations

**Days 51–60 · Result:** GitHub checks every change, builds a known image, and helps deploy it; you can monitor, secure, restore, and troubleshoot the Azure service with familiar commands.

Keep automation readable. A five-step workflow you understand is better than a copied enterprise pipeline.

## Day 51: Understand a GitHub Actions workflow

**Goal:** Read the basic parts of workflow YAML.

**Commands/concepts:** `.github/workflows`, `name`, `on`, `jobs`, `runs-on`, `steps`, `uses`, `run`.

**Task:** Read a minimal workflow that checks out the repository and prints Python/uv versions. Predict when it runs and what machine executes it, then add it on a branch.

**Done when:** The pull request shows one successful check and you can point to its trigger, job, runner, and steps.

**Resource:** [GitHub Actions quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart)

## Day 52: Run tests in CI

**Goal:** Make the same locked test command run locally and on GitHub.

**Commands:** `uv sync --locked`, `uv run pytest -q`; GitHub Actions logs.

**Task:** Extend the workflow to install `uv`, restore dependencies from the lockfile, and run tests. Introduce one harmless failing assertion, inspect the red log, fix it, and watch the check turn green.

**Done when:** GitHub blocks the broken change and the fixed commit passes without an API key or other secret.

**Resource:** [Official uv GitHub Actions guide](https://docs.astral.sh/uv/guides/integration/github/)

## Day 53: Build a Docker image in CI

**Goal:** Prove every change can produce a container from a clean runner.

**Commands/concepts:** `docker build`, image tag, build log, Git commit SHA.

**Task:** Add a second job that builds the Docker image, including the Dockerfile's training step, and tags it with the commit SHA. It does not publish yet.

**Done when:** A deliberately broken Dockerfile fails the job; after fixing it, the build passes and the log shows the intended tag.

**Resource:** [GitHub: publishing Docker images](https://docs.github.com/en/actions/use-cases-and-examples/publishing-packages/publishing-docker-images)

## Day 54: Publish an image to a registry

**Goal:** Store an immutable build that the VM can pull.

**Commands/concepts:** GitHub Container Registry, `docker login`, `docker pull`, tag versus digest, workflow `permissions`.

**Task:** On a version tag such as `v0.1.0`, publish the tested image to GHCR with minimal `packages: write` permission. On the VM, authenticate only if the package is private and pull the image.

**Done when:** Record the image name, version tag, commit SHA, and digest in `notes/release.md`; do not record tokens.

**Resource:** [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)

## Day 55: Deploy a known image safely

**Goal:** Deploy an identified image and keep a simple rollback target.

**Commands:** `docker compose pull`, `docker compose up -d`, `docker compose ps`, `curl`, `docker image inspect`.

**Task:** Change Compose on the VM to use the published version or digest instead of building. Pull, start, run `/health` and one prediction, and keep the previous image reference in the deployment note. Optionally trigger the same small script through a protected GitHub `staging` environment.

**Done when:** You can prove which commit/digest is running and switch back to the previous known image.

**Resources:** [GitHub deployment environments](https://docs.github.com/en/actions/reference/deployments-and-environments) · [Docker image digests](https://docs.docker.com/dhi/core-concepts/digests/)

## Day 56: Secure the VM and secrets

**Goal:** Reduce obvious exposure without pretending the practice VM is automatically production-grade.

**Commands/tools:** Azure NSG rules, `ss -lntp`, `sudo ufw status`, SSH configuration inspection, `docker inspect` with care.

**Task:** Confirm password SSH is disabled, port `22` is restricted to your IP, the API is loopback-only, unused inbound rules are removed, secrets are outside Git/images, and system packages are current. Understand that membership in the `docker` group is root-equivalent.

**Done when:** `notes/security-check.md` lists each verified control and remaining limitation without including secret values.

**Resources:** [Azure VM security recommendations](https://learn.microsoft.com/en-us/azure/virtual-machines/security-recommendations) · [Docker daemon attack surface](https://docs.docker.com/engine/security/)

## Day 57: Monitor the running service

**Goal:** Use one short checklist to answer whether the VM and app are healthy.

**Commands:** `uptime`, `htop`, `free -h`, `df -h`, `ss -lntp`, `docker ps`, `docker stats`, `docker logs --since`, `journalctl -u docker`, `curl`.

**Task:** Write `scripts/check-service.sh` to perform read-only checks for disk, memory, container status, and local `/health`. Then generate one prediction and find its log line.

**Done when:** The script clearly reports success/failure, and you can locate a CPU, memory, disk, container, port, or application problem with the appropriate command.

**Resource:** [Docker logs](https://docs.docker.com/reference/cli/docker/container/logs/)

## Day 58: Back up and restore the small app

**Goal:** Know what must be backed up and what can be rebuilt.

**Commands:** `tar`, `sha256sum`, `docker pull`, Git tags, the training command.

**Task:** Classify project state: source/synthetic data in Git, image in GHCR, configuration documented, secrets managed separately, and model reproducible from code/data. Delete only a disposable local model artifact, regenerate it, compare behavior, and rehearse pulling the known image on the VM.

**Done when:** `notes/recovery.md` states recovery order and proves the app can return from a missing container/model without relying on an untracked laptop file.

**Resource:** [GitHub releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)

## Day 59: Troubleshoot one failure end to end

**Goal:** Diagnose in layers instead of trying random fixes.

**Commands:** All earlier inspection commands; change only one controlled setting.

**Task:** Safely introduce one failure, such as a wrong container port or missing model path. Follow this order: reproduce with `curl`; check process/container; check listening port; read logs; check resources; inspect configuration; inspect recent Git/deployment changes. Fix it and verify recovery.

**Done when:** Complete the [troubleshooting note](../templates/troubleshooting-note.md) with symptom, evidence, cause, fix, and prevention.

**Resource:** [How to ask good debugging questions](https://stackoverflow.com/help/minimal-reproducible-example)

## Day 60: Final checkpoint redeploy and explain everything

**Goal:** Prove the fundamentals are connected and repeatable.

**Task:** Stop and remove the application containers, then redeploy the known image using only your README/runbook. Test health and prediction through the SSH tunnel. Show the GitHub checks, image digest, Azure resource map, process/container logs, and system resources.

**Done when:** In ten minutes, you can explain terminal → Git/GitHub → `uv`/Python → data/model → FastAPI → Docker image/container → registry → Azure resources/SSH → logs/health. Record a short demo and delete the Azure resource group when no longer needed.

**Resource:** [Simple runbook template](../templates/runbook.md)

### Final checkpoint

You are ready for a larger AI project when you can repeat the deployment, diagnose a broken port or model path, recover a known image, and explain every layer without handing the terminal to an AI assistant.
