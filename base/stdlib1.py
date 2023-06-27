from decimal import Decimal as dec

# >>> 0.1 + 0.1 + 0.1 == 0.3
# False
# >>>
# >>> dec('0.1') + dec('0.1') + dec('0.1') == dec('0.3')
# True
# >>>
# >>> dec(0.1)
# Decimal('0.1000000000000000055511151231257827021181583404541015625')
# >>>

# >>> dec('0.1')
# Decimal('0.1')
# >>>
# >>> dec(1) / dec(3)
# Decimal('0.3333333333333333333333333333')
# >>>
# >>> 1 + dec('0.2')
# Decimal('1.2')
# >>>
# >>> dec('0.2') - 8
# Decimal('-7.8')
# >>>
# >>> 25 ** dec('0.5')
# Decimal('5.000000000000000000000000000')
# >>>
# >>> 2 ** dec('0.5')
# Decimal('1.414213562373095048801688724')