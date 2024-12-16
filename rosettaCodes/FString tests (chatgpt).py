# Numeric formatting
print(f"Integer: {42:d}")
print(f"Floating-point with 2 decimals: {3.14159:.2f}")
print(f"Exponential notation: {123456:e}")
print(f"Hexadecimal: {255:x}")
print(f"Octal: {255:o}")
print(f"Binary: {255:b}")

# Alignment and padding
print(f"Right aligned with spaces: {'hello':>10}")
print(f"Left aligned with spaces: {'hello':<10}")
print(f"Center aligned with spaces: {'hello':^10}")
print(f"Right aligned with zeros: {42:05}")
print(f"Left aligned with dots: {42:.<10}")
print(f"Center aligned with underscores: {42:_^10}")

# String formatting
print(f"Uppercase: {'hello':^10s}".upper())
print(f"Lowercase: {'HELLO':<10s}".lower())

# String with slicing
name = "Alice"
print(f"First 3 characters: {name:.3s}")
print(f"Full name padded: {name:*^10s}")

# Compound expressions
x, y = 3, 4
print(f"Sum of {x} and {y}: {x + y}")
print(f"Formatted sum: {x + y:04}")

# Escape sequences
print(f"Curly braces escaped: {{Hello}}")
print(f"Newline character: {'Line1\\nLine2':<15s}")
print(f"Tab character: {'Column1\\tColumn2':<20s}")

# Complex nested f-strings
nested = f"{'nested':>10}"
print(f"Outer string with {nested}")

# Date and time formatting
from datetime import datetime
now = datetime(2023, 1, 1, 12, 0, 0)  # January 1, 2023, at 12:00:00
print(f"Current date and time: {now:%Y-%m-%d %H:%M:%S}")
print(f"Year: {now:%Y}, Month: {now:%m}, Day: {now:%d}")

# Percent formatting
print(f"Percentage: {0.856:.2%}")

# Conditional formatting
value = 42
print(f"Positive or Negative: {value:+d}")
print(f"Zero-padded negative: {-42:05d}")

# Chained calculations
width, height = 5, 10
area = width * height
print(f"Rectangle {width}x{height} has area {area}")
