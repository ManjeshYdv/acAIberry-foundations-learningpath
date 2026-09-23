# Day 17: Inspect Services with systemctl and journalctl

**Tue Sep 23**

**Time spent: 1:00 PM to 2:00 PM**

## Goal

Understand that a Linux service has its own status and system logs, which are separate from the terminal where commands are executed.

## Commands I practiced

```text
systemctl status
systemctl list-units --type=service
journalctl -u
journalctl --since
```

## What I learned

### What is a service?

A **service** is a background process managed by the operating system, usually used to provide a specific function continuously or when needed.


Commit, file, screenshot, command output, or URL:

## Proof of Learning

* Checked service status using `systemctl status`.
* Inspected services with `systemctl list-units`.
* Filtered services by type: `service`, `timer`, and `target`.
* Viewed Docker logs using `journalctl -u docker --since today`.
* Practiced identifying command typos and incorrect options.


## Can I explain it without AI?

* [✓] Yes
* [ ] Not yet; repeat this day
