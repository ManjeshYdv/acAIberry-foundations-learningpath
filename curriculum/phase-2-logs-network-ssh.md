# Phase 2: Logs, Errors, Networks, and SSH

**Days 11–20 · Result:** you can read an error, inspect a log, find a listening service, test it with `curl`, and prepare for remote access with SSH.

Keep using the same project. The small servers and broken files in this phase are safe practice targets for later Azure troubleshooting.

## Day 11: Understand output, errors, and exit codes

**Goal:** Separate normal output from error output and know whether a command succeeded.

**Commands:** `echo $?`, `>`, `2>`, `2>&1`.

**Task:** Run one valid `ls` and one invalid `ls`. Save normal output to `logs/output.log` and errors to `logs/error.log`. Check the exit code immediately after each command.

**Done when:** You can explain stdout, stderr, exit code `0`, and a non-zero exit code.

**Resource:** [Bash manual: redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html)

## Day 12: Read changing logs with tail

**Goal:** Follow a log and filter the lines that matter.

**Commands:** `tail -n`, `tail -f`, `grep -i`, `grep -C`, `less +G`.

**Task:** In one terminal, run `tail -f logs/app.log`. In another, append `INFO`, `WARNING`, and `ERROR` lines. Find the last error and show two surrounding lines.

**Done when:** You can follow a live log, stop following with `Ctrl+C`, and save the relevant error context rather than the whole file.

**Resource:** [GNU `tail` documentation](https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html)

## Day 13: Read a Python traceback

**Goal:** Read errors from the bottom up and distinguish exception type, message, file, and line number.

**Commands:** `python3`, `nano`, `tail`, `grep`.

**Task:** Create a short Python file that reads a missing dictionary key. Run it, redirect the traceback to `logs/python-error.log`, identify the failing line, fix it safely, and run it again.

**Done when:** `notes/error-reading.md` records the exception type, message, exact line, cause, and fix.

**Resource:** [Python errors and exceptions](https://docs.python.org/3/tutorial/errors.html)

## Day 14: Understand permissions and sudo

**Goal:** Read Linux permissions and change only what is necessary.

**Commands:** `ls -l`, `chmod u+x`, `chmod 600`, `id`, `groups`, `sudo -l`.

**Task:** Make `scripts/system-report.sh` executable for its owner and make a dummy secret file readable only by its owner. Inspect before and after permissions. Delete the dummy content when finished.

**Done when:** You can explain owner/group/other and read/write/execute. You did not use `chmod 777` or run the project as root.

**Resource:** [Linux Journey: file permissions](https://linuxjourney.com/lesson/file-permissions)

## Day 15: Use environment variables and PATH

**Goal:** Understand configuration passed through the environment and how the shell finds commands.

**Commands:** `env`, `printenv`, `export`, `PATH`, `which`, `type`.

**Task:** Export `APP_ENV=development`, read it from a tiny Python script, and create `.env.example` with a safe placeholder. Do not put a real secret in it.

**Done when:** You can explain why the variable disappears in a fresh terminal and why `.env` must be ignored by Git later.

**Resource:** [The Twelve-Factor App: config](https://12factor.net/config)

## Day 16: Install and inspect packages

**Goal:** Use the operating-system package manager deliberately.

**Commands:** `apt search`, `apt show`, `sudo apt update`, `sudo apt install`, `dpkg -l`.

**Task:** Search for and inspect `htop`, `curl`, and `ripgrep`. Install only missing tools, then confirm their paths and versions. On non-Ubuntu systems, use the equivalent package manager.

**Done when:** `notes/tools.md` records the command, version, and why each tool is needed.

**Resource:** [Ubuntu package management](https://documentation.ubuntu.com/server/how-to/software/package-management/)

## Day 17: Inspect services with systemctl and journalctl

**Goal:** Understand that a service has status and system logs separate from your terminal.

**Commands:** `systemctl status`, `systemctl list-units --type=service`, `journalctl -u`, `journalctl --since`.

**Task:** Choose one existing service such as `ssh`, `cron`, or Docker. Inspect its status and today's logs. Do not restart a service you do not understand.

**Done when:** Save the service state, main PID, last five relevant log lines, and the command used in `notes/service-check.md`.

**Resource:** [systemctl manual](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)

## Day 18: Understand IP addresses, DNS, and ports

**Goal:** Know the difference between a host, IP address, DNS name, port, and listening process.

**Commands:** `ip addr`, `hostname -I`, `getent hosts`, `ss -lntp`.

**Task:** Start `python3 -m http.server 8000` in the project. In another terminal, find the listening port and process. Resolve one public hostname with `getent hosts`.

**Done when:** You can point to the local address, port `8000`, and PID and explain why `127.0.0.1` is not publicly reachable.

**Resource:** [Cloudflare: what is a port?](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)

## Day 19: Inspect HTTP with curl

**Goal:** Send an HTTP request and read the status, headers, and body.

**Commands:** `curl -i`, `curl -v`, `curl -sS`, `curl -o`, `curl -w`.

**Task:** Request an existing file and a missing file from the local server. Compare `200` and `404`, then capture only the status code.

**Done when:** `notes/http.md` explains request method, URL, status code, headers, body, and what `404` means.

**Resource:** [MDN: HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)

## Day 20: Checkpoint diagnose a local server

**Goal:** Use processes, logs, ports, and HTTP together, then prepare an SSH identity for the Azure phase.

**Commands:** `ps`, `ss`, `tail`, `grep`, `curl`, `kill`, `ssh-keygen`, `ssh -i`.

**Task:** Start the local server in the background with stdout/stderr redirected to `logs/server.log`. Find its PID and port, request a missing path, locate the `404` in the log, and stop it normally. Then create a dedicated Ed25519 practice key and protect the private key; never print or commit it.

**Done when:** `notes/day-20-diagnosis.md` shows the symptom, commands, evidence, cause, and fix, plus the general future command `ssh -i KEY user@host` with placeholders only.

**Resources:** [GitHub SSH key guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) · [OpenSSH manual](https://www.openssh.com/manual.html)

### Phase checkpoint

Start the server with a log file and ask someone to name either a PID, port, HTTP error, or log message for you to find. Use evidence, not guesswork.
