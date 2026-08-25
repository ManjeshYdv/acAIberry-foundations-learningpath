# Phase 1: Linux Essentials

**Days 1–10 · Result:** you can move around a Linux system, inspect files and processes, and produce a small system report without copying a long command blindly.

Work inside one `ticket-classifier` folder. Save short notes under `notes/` and scripts under `scripts/` so every exercise contributes to the same project.

## Day 1: Open the terminal and create the project

**Goal:** Know where you are, which user and machine you are using, and how to ask a command for help.

**Commands:** `mkdir -p`, `whoami`, `hostname`, `date`, `uname -a`, `man`, `--help`, `clear`.

**Task:** Create `ticket-classifier` with `notes`, `scripts`, `data`, and `logs` directories. Run the system-information commands and save their output or a screenshot as the first daily proof. Read the help for `ls` instead of trying to memorize every option.

**Done when:** You can explain user, host, operating system/kernel, current date, and how to exit a manual page (`q`).

**Resource:** [The Missing Semester: shell](https://missing.csail.mit.edu/2020/course-shell/)

## Day 2: Navigate with pwd, ls, and cd

**Goal:** Understand absolute paths, relative paths, the home directory, and the current directory.

**Commands:** `pwd`, `ls`, `ls -la`, `cd`, `cd ..`, `cd -`, `~`.

**Task:** Navigate from your home directory into the project, into `notes`, back to the project, and back to the previous directory. Add the paths you visited to `notes/paths.txt`.

**Done when:** You can reach the project from anywhere using both an absolute and relative path.

**Resource:** [Linux Journey: the shell](https://linuxjourney.com/lesson/the-shell)

## Day 3: Create, copy, move, and remove files

**Goal:** Change the filesystem carefully and understand the difference between a file and directory.

**Commands:** `mkdir -p`, `touch`, `cp -i`, `mv -i`, `rm -i`, `rmdir`.

**Task:** Under `data/practice`, create three ticket text files, copy one, rename the copy, and remove only the copy. Use interactive flags while learning. Do not practice recursive deletion.

**Done when:** `data/practice` contains exactly the three intended files and you can describe each command you used.

**Resource:** [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)

## Day 4: Read files without opening an editor

**Goal:** Choose the right tool for a short file, a long file, or only part of a file.

**Commands:** `cat`, `less`, `head`, `tail`, `wc -l`, `file`.

**Task:** Add ten one-line sample tickets to `data/tickets.txt`. View all tickets, only the first three, only the last three, and count the lines.

**Done when:** You can inspect a long file with `less`, search inside it with `/text`, and exit with `q`.

**Resource:** [GNU `less` manual](https://www.greenwoodsoftware.com/less/)

## Day 5: Edit safely with Nano

**Goal:** Make a small terminal edit without becoming trapped in the editor.

**Commands:** `nano filename`; inside Nano use `Ctrl+O` to save, `Enter` to confirm, `Ctrl+W` to search, and `Ctrl+X` to exit.

**Task:** Open `data/tickets.txt`, format each line as `label | message`, and use labels such as `billing`, `account`, and `technical`. Correct one line, search for one label, save, and exit.

**Done when:** Reopening the file shows the saved change and you can leave Nano without terminating the terminal.

**Resource:** [GNU Nano manual](https://www.nano-editor.org/dist/latest/nano.html)

## Day 6: Search text with grep and ripgrep

**Goal:** Find useful lines in files without reading everything.

**Commands:** `grep`, `grep -n`, `grep -i`, `grep -r`, `rg`.

**Task:** Find all billing tickets, case-insensitive occurrences of “error,” and every file containing “password.” Compare recursive `grep` with `rg` if ripgrep is installed.

**Done when:** Save three useful search commands in `notes/searches.md` and explain the filename, line number, and matching text in the output.

**Resource:** [ripgrep guide](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md)

## Day 7: Combine commands with pipes

**Goal:** Pass the output of one command into another and save output intentionally.

**Commands:** `|`, `>`, `>>`, `cut`, `sort`, `uniq -c`, `tee`.

**Task:** Extract ticket labels, sort them, count each unique label, and save the summary to `notes/label-counts.txt`. Run it again with `tee` so you can see and save the output.

**Done when:** You can explain why `>` replaces a file, `>>` appends, and a pipe does not automatically save anything.

**Resource:** [The Missing Semester: data wrangling](https://missing.csail.mit.edu/2020/data-wrangling/)

## Day 8: Inspect processes with ps, top, and htop

**Goal:** Understand a running process, its PID, CPU/memory usage, and graceful termination.

**Commands:** `sleep 300 &`, `jobs`, `ps aux`, `pgrep`, `top`, `htop`, `kill`, `fg`.

**Task:** Start a background `sleep` process, find it in `ps` and `htop`, note its PID, then stop it with normal `kill`. Do not use `kill -9` unless a normal termination has failed.

**Done when:** The process is gone and `notes/processes.md` explains PID, foreground, background, CPU, memory, and `SIGTERM` in your own words.

**Resource:** [Linux Journey: processes](https://linuxjourney.com/lesson/monitor-processes-ps-command)

## Day 9: Check disk and memory

**Goal:** Distinguish disk space, directory size, and RAM usage.

**Commands:** `df -h`, `du -sh`, `du -h --max-depth=1`, `free -h`, `uptime`, `lscpu`; optionally `nvidia-smi` if a GPU exists.

**Task:** Measure free disk space, project size, largest top-level project directory, memory use, system load, and CPU count. If a GPU exists, inspect it without changing settings. Add the values to `notes/resources.md`.

**Done when:** You can answer “Is the disk full?” and “Is memory under pressure?” with the correct command output.

**Resource:** [Ubuntu Server documentation](https://documentation.ubuntu.com/server/)

## Day 10: Checkpoint build a system report

**Goal:** Connect the first nine days in one repeatable, read-only script.

**Commands:** `#!/usr/bin/env bash`, `echo`, `date`, `whoami`, `hostname`, `df`, `free`, `ps`, `bash`.

**Task:** Create `scripts/system-report.sh`. It should print the date, user, host, project size, disk usage, memory usage, and the five processes using the most memory. It must only read system information.

**Done when:** `bash scripts/system-report.sh > notes/system-report.txt` succeeds, the output is understandable, and you can explain every line of the script.

**Resource:** [ShellCheck](https://www.shellcheck.net/)

### Phase checkpoint

Without notes, navigate to the project, edit a file with Nano, find a label with `grep`, inspect a process with `htop`, and check disk and memory. Repeat any step that still feels like guesswork.
