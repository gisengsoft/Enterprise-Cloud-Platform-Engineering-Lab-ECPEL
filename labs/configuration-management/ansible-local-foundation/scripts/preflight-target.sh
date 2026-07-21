#!/usr/bin/env bash
set -euo pipefail

fail() { printf 'preflight failed: %s\n' "$1" >&2; exit 1; }

[[ "$(uname -s)" == Linux ]] || fail 'Linux is required'
[[ -r /proc/version ]] || fail 'kernel version metadata is unavailable'
if ! tr '[:upper:]' '[:lower:]' < /proc/version | grep -q 'microsoft'; then
  fail 'WSL kernel indicator is required'
fi
[[ -d /run/WSL ]] || fail 'WSL runtime directory indicator is required'
[[ "${WSL_DISTRO_NAME:-}" == ecpel-ansible-local-foundation ]] || fail 'approved WSL distribution name is required'
case "${WSL_DISTRO_NAME:-}" in Ubuntu-22.04|docker-desktop) fail 'reserved distribution must not be targeted' ;; esac
[[ -r /etc/os-release ]] || fail 'os-release is unavailable'
. /etc/os-release
[[ "${ID:-}" == ubuntu ]] || fail 'Ubuntu is required'
[[ "${VERSION_ID:-}" == 24.04 ]] || fail 'Ubuntu 24.04 is required'
[[ -d /run/systemd/system ]] || fail 'operational systemd is required'
python3.12 --version >/dev/null 2>&1 || fail 'Python 3.12 is required'
case "${PWD}" in /mnt/*) fail 'repository path under /mnt is not approved' ;; esac
[[ -d /opt || -w /opt ]] || fail 'approved destination root must be available'
[[ -z "${ANSIBLE_HOST:-}" && -z "${ANSIBLE_REMOTE_USER:-}" && -z "${ANSIBLE_PRIVATE_KEY_FILE:-}" ]] || fail 'remote Ansible configuration is not approved'
printf 'preflight passed for approved simulated local target\n'
