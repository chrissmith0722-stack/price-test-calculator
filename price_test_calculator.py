#!/usr/bin/env python3
"""Compare $9 / $19 / $27 digital product price outcomes."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


PRICES = (9, 19, 27)


@dataclass
class Row:
    price: int
    conversion: float
    sales: float
    revenue: float
    contribution: float


def prompt_float(label: str, default: float | None = None) -> float:
    suffix = f" [{default}]" if default is not None else ""
    while True:
        raw = input(f"{label}{suffix}: ").strip()
        if not raw and default is not None:
            return default
        try:
            return float(raw)
        except ValueError:
            print("  enter a number")


def build_rows(visitors: float, conversions: dict[int, float], cost: float) -> list[Row]:
    rows: list[Row] = []
    for price in PRICES:
        conv = conversions[price]
        sales = visitors * conv
        revenue = sales * price
        contribution = sales * (price - cost)
        rows.append(Row(price, conv, sales, revenue, contribution))
    return rows


def print_table(rows: list[Row]) -> None:
    print()
    print(f"{'Price':>5} | {'Conv%':>6} | {'Sales':>6} | {'Revenue':>8} | {'Contrib$':>8}")
    print("-" * 5 + "-+-" + "-" * 6 + "-+-" + "-" * 6 + "-+-" + "-" * 8 + "-+-" + "-" * 8)
    for r in rows:
        print(
            f"${r.price:>3} | {r.conversion * 100:5.2f}% | {r.sales:6.0f} | "
            f"${r.revenue:7.2f} | ${r.contribution:7.2f}"
        )
    best = max(rows, key=lambda r: r.contribution)
    print()
    print(f"Suggested starting price by contribution: ${best.price}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Price ladder calculator for digital products")
    parser.add_argument("--visitors", type=float, help="Monthly visitors / sessions")
    parser.add_argument("--conv-9", type=float, help="Conversion rate at $9 (e.g. 0.04)")
    parser.add_argument("--conv-19", type=float, help="Conversion rate at $19")
    parser.add_argument("--conv-27", type=float, help="Conversion rate at $27")
    parser.add_argument("--cost", type=float, help="Variable cost per sale (fees, delivery, etc.)")
    args = parser.parse_args()

    visitors = args.visitors if args.visitors is not None else prompt_float("Monthly visitors", 1000)
    conv9 = args.conv_9 if args.conv_9 is not None else prompt_float("Conversion at $9 (0-1)", 0.04)
    conv19 = args.conv_19 if args.conv_19 is not None else prompt_float("Conversion at $19 (0-1)", 0.025)
    conv27 = args.conv_27 if args.conv_27 is not None else prompt_float("Conversion at $27 (0-1)", 0.015)
    cost = args.cost if args.cost is not None else prompt_float("Cost per sale $", 1.0)

    rows = build_rows(visitors, {9: conv9, 19: conv19, 27: conv27}, cost)
    print_table(rows)


if __name__ == "__main__":
    main()
