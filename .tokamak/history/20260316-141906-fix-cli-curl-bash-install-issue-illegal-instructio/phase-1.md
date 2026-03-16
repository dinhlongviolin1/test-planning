# Implement CPU-aware install script (phase-1)

**Date**: 2026-03-16

## Task 1.1: Create CPU-aware install.sh script and issue tracking file i-015.md
**Status**: in_progress
**Summary**: Created `install.sh` with full CPU capability detection to prevent "Illegal instruction" crashes, and `issues/i-015.md` tracking the fix. The script detects AVX-512/AVX2 support on Linux via `/proc/cpuinfo` and on macOS via `sysctl`, then downloads the matching binary variant.

**Files Changed**:
- .gitignore (+2, -0)
- .tokamak/history/20260316-141906-fix-cli-curl-bash-install-issue-illegal-instructio/phase-1.md (+3, -0)
- .tokamak/history/20260316-141906-fix-cli-curl-bash-install-issue-illegal-instructio/run.md (+6, -0)
- install.sh (+186, -0)
- issues/i-015.md (+37, -0)
