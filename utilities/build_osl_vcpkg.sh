#!/usr/bin/env bash
set -e

### Usage
# export VCPKG_ROOT=/path/to/vcpkg
# ./build_osl.sh minimal
# ./build_osl.sh python+testrender

# --- Parse args ---
variant="minimal"
if [ $# -gt 0 ]; then
  variant="$1"
fi

# --- Set VCPKG_ROOT ---
: "${VCPKG_ROOT:=$HOME/vcpkg}"
if [ ! -d "$VCPKG_ROOT" ]; then
  echo "Error: VCPKG_ROOT directory does not exist: $VCPKG_ROOT"
  exit 1
fi

# --- Print build info ---
echo "Building OSL variant: $variant"
echo "Using vcpkg at: $VCPKG_ROOT"

# --- Detect OS and set triplet, generator, and vcpkg binary ---
case "$OSTYPE" in
  msys*|cygwin*|win32*)
    triplet="x64-windows-release"
    generator="-GVisual Studio 17 2022 -A x64"
    vcpkg_bin="$VCPKG_ROOT/vcpkg.exe"
    ;;
  linux*)
    triplet="x64-linux-release"
    generator="-GNinja"
    vcpkg_bin="$VCPKG_ROOT/vcpkg"
    ;;
  darwin*)
    triplet="x64-osx-release"
    generator="-GNinja"
    vcpkg_bin="$VCPKG_ROOT/vcpkg"
    ;;
  *)
    echo "Unsupported OS: $OSTYPE"
    exit 1
    ;;
esac

if [ ! -f "$vcpkg_bin" ]; then
  echo "Error: vcpkg binary not found at $vcpkg_bin"
  exit 1
fi

echo "Using vcpkg binary: $vcpkg_bin"
echo "Using vcpkg triplet: $triplet"
echo "Using CMake generator: $generator"

# --- Select dependencies and CMake options ---
if [ "$variant" = "minimal" ]; then
  deps=("llvm" "boost" "openimageio" "openexr")
  cmake_opts="-DOSL_BUILD_TESTRENDER=OFF -DOSL_BUILD_PYTHON=OFF"
elif [ "$variant" = "python+testrender" ]; then
  deps=("llvm" "boost" "openimageio" "openexr" "glew" "opengl" "python3" "pybind11")
  cmake_opts="-DOSL_BUILD_TESTRENDER=ON -DOSL_BUILD_PYTHON=ON"
else
  echo "Unknown variant: $variant"
  echo "Usage: $0 [minimal|python+testrender]"
  exit 1
fi

# --- Install missing dependencies only (Release-only) ---
missing=()
for dep in "${deps[@]}"; do
  if ! "$vcpkg_bin" list | grep -q "^$dep:"; then
    missing+=("$dep")
  fi
done

if [ ${#missing[@]} -gt 0 ]; then
  echo "Installing missing dependencies (Release-only): ${missing[*]}"
  "$vcpkg_bin" install "${missing[@]}" --triplet $triplet
else
  echo "All dependencies already installed (Release-only)."
fi

# --- Configure CMake ---
cmake -S . -B build \
  $generator \
  -DCMAKE_TOOLCHAIN_FILE="$VCPKG_ROOT/scripts/buildsystems/vcpkg.cmake" \
  -DCMAKE_BUILD_TYPE=Release \
  $cmake_opts

# --- Build ---
cmake --build build --config Release
