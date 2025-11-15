#!/usr/bin/env python3
"""
slang_compile.py

Usage:
    python slang_compile.py shader.slang
    python slang_compile.py shader.slang --targets glsl,spirv,msl
    python slang_compile.py shader.slang --slang-dir path/to/extracted/slang

This script finds the slangc executable and invokes it for the selected targets.
It prefers an explicit --slang-dir if provided (where releases unpack to).
"""

import shutil
import subprocess
import sys
import os
import argparse

# Mapping of logical targets to slangc CLI flags and default extra args
TARGETS = {
    "hlsl": {
        "target_flag": "hlsl",
        "extra": [],  # you can pass -profile if wanted, e.g. "sm_6_3"
        "outfile_ext": "hlsl",
    },
    "glsl": {
        "target_flag": "glsl",
        "extra": ["-profile", "glsl_460"],  # reasonable default
        "outfile_ext": "glsl",
    },
    "spirv": {
        "target_flag": "spirv",
        # emit SPIR-V directly (binary) by default. If you want a text form, remove -emit-spirv-directly.
        "extra": ["-emit-spirv-directly", "-fvk-use-entrypoint-name"],
        "outfile_ext": "spv",
    },
    "msl": {
        "target_flag": "metal",
        "extra": [],  # you may want -profile msl_2_0 etc depending on needs
        "outfile_ext": "metal",
    },
    "cuda": {
        "target_flag": "cuda",
        "extra": [],
        "outfile_ext": "cu",
    },
    "wgsl": {
        "target_flag": "wgsl",
        "extra": [],   # you can add specific flags if needed
        "outfile_ext": "wgsl",
    },
}

def find_slangc(slang_dir=None):
    # 1) If user gave a slang_dir, look for slangc(.exe) there
    candidate_names = ["slangc", "slangc.exe"]
    if slang_dir:
        for name in candidate_names:
            p = os.path.join(slang_dir, name)
            if os.path.isfile(p) and os.access(p, os.X_OK):
                return os.path.abspath(p)

        # sometimes releases put binaries in bin/
        for name in candidate_names:
            p = os.path.join(slang_dir, "bin", name)
            if os.path.isfile(p) and os.access(p, os.X_OK):
                return os.path.abspath(p)

    # 2) Try PATH
    p = shutil.which("slangc")
    if p:
        return p

    # 3) Try current directory
    for name in candidate_names:
        if os.path.isfile(name) and os.access(name, os.X_OK):
            return os.path.abspath(name)

    raise FileNotFoundError(
        "Could not find 'slangc' executable. "
        "Provide --slang-dir pointing at an extracted release directory, or put 'slangc' on PATH."
    )

def build_output_name(input_path, target_key):
    base = os.path.splitext(os.path.basename(input_path))[0]
    ext = TARGETS[target_key]["outfile_ext"]
    return f"{base}.{ext}"

def run_slangc(slangc_path, input_path, out_path, target_key, extra_args):
    cfg = TARGETS[target_key]
    target_flag = cfg["target_flag"]

    cmd = [slangc_path, input_path, "-target", target_flag]

    # append extras from mapping then extras passed to function
    cmd += cfg.get("extra", []) + (extra_args or [])

    # Correct: for entry-point targets, put '-entry main' before '-o'
    cmd += ["-entry", "main", "-o", out_path]

    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0:
        print(f"Error: slangc failed for target {target_key}.")
        print("stdout:")
        print(proc.stdout)
        print("stderr:")
        print(proc.stderr)
        raise RuntimeError(f"slangc failed (returncode={proc.returncode})")
    if proc.stdout.strip():
        print(proc.stdout)
    if proc.stderr.strip():
        print(proc.stderr)
    print(f"Generated {out_path}")


def run_slangc2(slangc_path, input_path, out_path, target_key, extra_args):
    cfg = TARGETS[target_key]
    target_flag = cfg["target_flag"]

    cmd = [slangc_path, input_path, "-target", target_flag]

    # append extras from mapping then extras passed to function
    cmd += cfg.get("extra", []) + (extra_args or [])

    # specify output - slangc uses -o for output file (observed in docs)
    cmd += ["-o", out_path]

    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0:
        print(f"Error: slangc failed for target {target_key}.")
        print("stdout:")
        print(proc.stdout)
        print("stderr:")
        print(proc.stderr)
        raise RuntimeError(f"slangc failed (returncode={proc.returncode})")
    # Print diagnostic output if any
    if proc.stdout.strip():
        print(proc.stdout)
    if proc.stderr.strip():
        print(proc.stderr)
    print(f"Generated {out_path}")

def main():
    ap = argparse.ArgumentParser(description="Compile a slang shader to multiple targets using slangc.")
    ap.add_argument("input", help="Input .slang file")
    ap.add_argument(
        "--targets", "-t",
        default="hlsl,glsl,spirv,msl,cuda,wgsl",
        help="Comma-separated list of targets. Supported: " + ",".join(TARGETS.keys())
    )
    ap.add_argument("--slang-dir", help="Path to extracted slang release (optional)")
    ap.add_argument("--extra", "-e", action="append", help="extra flags to pass to slangc (applies to all targets).")
    ap.add_argument("--out-dir", "-o", default=".", help="Directory to write outputs to.")
    args = ap.parse_args()

    input_path = args.input
    if not os.path.isfile(input_path):
        print("Input file not found:", input_path)
        sys.exit(2)

    try:
        slangc = find_slangc(args.slang_dir)
    except FileNotFoundError as ex:
        print(ex)
        sys.exit(2)

    chosen = [t.strip().lower() for t in args.targets.split(",") if t.strip()]
    for t in chosen:
        if t not in TARGETS:
            print("Unknown target:", t)
            print("Supported:", ", ".join(TARGETS.keys()))
            sys.exit(2)

    os.makedirs(args.out_dir, exist_ok=True)

    extra_args = []
    if args.extra:
        # flatten list of extra strings
        for ea in args.extra:
            extra_args += ea.split()

    for t in chosen:
        out_name = build_output_name(input_path, t)
        out_path = os.path.join(args.out_dir, out_name)
        run_slangc(slangc, input_path, out_path, t, extra_args)

if __name__ == "__main__":
    main()
