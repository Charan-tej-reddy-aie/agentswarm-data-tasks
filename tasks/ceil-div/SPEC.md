# Compute integer ceiling division

Implement ceil_div(number, divisor) in ceil_div.py using Python 3.11+ standard
library only. This tiny task needs no dependencies. Only edit ceil_div.py and
optional IMPLEMENTATION.md. Both arguments must have exact built-in int type;
bool, int subclasses, floats, strings, None and containers raise TypeError.
Check both types before bounds: (1.0,0) raises TypeError. For integer inputs,
divisor <= 0 raises ValueError. Exception messages are unconstrained.

Return the mathematical ceiling of number/divisor as an exact built-in int.
number may be negative, zero or positive; integers have arbitrary precision.
Use integer arithmetic without float conversion. Calls are deterministic and
have no side effects or mutable global state. Examples: (7,3)->3; (6,3)->2;
(-7,3)->-2; (-6,3)->-2; (0,3)->0; (1,10)->1; (3,0) raises ValueError;
(True,3) and (1.0,0) raise TypeError. Every example is checked.
There is no tokenization or object coercion. No packages, files, network, clock,
README-dependent checks or production claims. Source/scope review accompanies
public fixtures and Docker --network none acceptance.
