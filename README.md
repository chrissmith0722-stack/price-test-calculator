# price-test-calculator

Quick math for testing digital-product price points at **$9 / $19 / $27**.

Given monthly visitors, conversion rate guesses, and variable cost per sale, print a comparison table of expected sales and contribution margin.

## Requirements

- Python 3.9+

## Usage

```bash
python price_test_calculator.py \
  --visitors 2000 \
  --conv-9 0.04 \
  --conv-19 0.025 \
  --conv-27 0.015 \
  --cost 1.50
```

Interactive prompts are used for any flag you omit.

These are planning estimates — not financial advice.

## License

MIT
