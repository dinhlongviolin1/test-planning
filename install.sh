#!/usr/bin/env bash
set -euo pipefail

# Base URL for binary releases — change this to point to a different release server
base_url="https://releases.tokamak.sh"

# ---------------------------------------------------------------------------
# OS detection
# ---------------------------------------------------------------------------
detect_os() {
    local raw_os
    raw_os="$(uname -s | tr '[:upper:]' '[:lower:]')"
    case "${raw_os}" in
        linux)  echo "linux" ;;
        darwin) echo "darwin" ;;
        *)
            echo "Unsupported OS: ${raw_os}. Only Linux and macOS are supported." >&2
            exit 1
            ;;
    esac
}

# ---------------------------------------------------------------------------
# Architecture detection
# ---------------------------------------------------------------------------
detect_arch() {
    local raw_arch
    raw_arch="$(uname -m)"
    case "${raw_arch}" in
        x86_64)           echo "amd64" ;;
        aarch64 | arm64)  echo "arm64" ;;
        *)
            echo "Unsupported architecture: ${raw_arch}. Only x86_64 and aarch64/arm64 are supported." >&2
            exit 1
            ;;
    esac
}

# ---------------------------------------------------------------------------
# CPU variant detection
# Returns 'avx512', 'avx2', or 'generic'.
# Only meaningful for amd64 — arm64 always gets 'generic'.
# ---------------------------------------------------------------------------
detect_cpu_variant() {
    local os="${1}"
    local arch="${2}"

    # ARM never has AVX extensions; ship the generic arm64 binary
    if [ "${arch}" = "arm64" ]; then
        echo "generic"
        return
    fi

    if [ "${os}" = "linux" ]; then
        local flags
        flags="$(grep -m1 '^flags' /proc/cpuinfo 2>/dev/null || true)"
        if echo "${flags}" | grep -q 'avx512f'; then
            echo "avx512"
        elif echo "${flags}" | grep -q 'avx2'; then
            echo "avx2"
        else
            echo "generic"
        fi
    elif [ "${os}" = "darwin" ]; then
        local features
        features="$(sysctl -n machdep.cpu.features machdep.cpu.leaf7_features 2>/dev/null || true)"
        if echo "${features}" | grep -qi 'AVX512F'; then
            echo "avx512"
        elif echo "${features}" | grep -qi 'AVX2'; then
            echo "avx2"
        else
            echo "generic"
        fi
    else
        # Fallback for any future OS — ship the portable generic binary
        echo "generic"
    fi
}

# ---------------------------------------------------------------------------
# Binary name construction
# ---------------------------------------------------------------------------
build_binary_name() {
    local os="${1}"
    local arch="${2}"
    local variant="${3}"

    if [ "${arch}" = "arm64" ]; then
        echo "tokamak-${os}-arm64"
    elif [ "${variant}" = "avx512" ]; then
        echo "tokamak-${os}-amd64-avx512"
    elif [ "${variant}" = "avx2" ]; then
        echo "tokamak-${os}-amd64-avx2"
    else
        echo "tokamak-${os}-amd64"
    fi
}

# ---------------------------------------------------------------------------
# Download helper — prefers curl, falls back to wget
# ---------------------------------------------------------------------------
download() {
    local url="${1}"
    local dest="${2}"

    if command -v curl >/dev/null 2>&1; then
        curl -fsSL "${url}" -o "${dest}"
    elif command -v wget >/dev/null 2>&1; then
        wget -qO "${dest}" "${url}"
    else
        echo "Neither curl nor wget found. Please install one and retry." >&2
        exit 1
    fi
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
main() {
    local no_auth=false

    for arg in "$@"; do
        case "${arg}" in
            --no-auth) no_auth=true ;;
            *) ;;
        esac
    done

    local os arch variant binary download_url

    os="$(detect_os)"
    arch="$(detect_arch)"
    variant="$(detect_cpu_variant "${os}" "${arch}")"
    binary="$(build_binary_name "${os}" "${arch}" "${variant}")"
    download_url="${base_url}/${binary}"

    # Determine install destination
    local install_dest
    if [ "$(id -u)" -eq 0 ]; then
        install_dest="/usr/local/bin/tokamak"
    else
        install_dest="${HOME}/.local/bin/tokamak"
    fi

    local install_dir
    install_dir="$(dirname "${install_dest}")"
    mkdir -p "${install_dir}"

    # Temp dir cleaned up automatically on exit
    local tmp_dir
    tmp_dir="$(mktemp -d)"
    trap 'rm -rf "${tmp_dir}"' EXIT

    local tmp_bin="${tmp_dir}/tokamak"

    echo "Downloading ${binary}..."
    if ! download "${download_url}" "${tmp_bin}"; then
        echo "Download failed for URL: ${download_url}" >&2
        echo "Please check your internet connection or file an issue if the binary is missing." >&2
        exit 1
    fi

    chmod +x "${tmp_bin}"
    mv "${tmp_bin}" "${install_dest}"

    echo "✓ Installed tokamak to ${install_dest}"

    # Warn if the install directory is not on PATH
    case ":${PATH}:" in
        *":${install_dir}:"*) ;;
        *)
            echo "Warning: ${install_dir} is not in your PATH." >&2
            echo "Add the following to your shell profile:" >&2
            echo "  export PATH=\"${install_dir}:\${PATH}\"" >&2
            ;;
    esac

    # Run auth using the exact binary we just installed, not whatever 'tokamak' resolves
    # to in PATH — this is important so the CPU-compatible binary handles auth
    if [ "${no_auth}" = false ]; then
        echo "i Starting authentication..."
        "${install_dest}" auth </dev/tty
    fi
}

main "$@"
