
from sample_tube import SampleTube, InsufficientVolumeError
from sample_transaction import SampleEvent

# Fresh tube
t1 = SampleTube("DNA_A")
print(t1) # expect repr to include label and vol=0µL

# Add volume
e1 = t1.add_volume(120, memo="resuspension")
assert t1.volume_uL == 120 and e1.volume_change_uL == 120

# Consume volume
e2 = t1.consume_volume(20, memo="PCR setup")
assert t1.volume_uL == 100 and e2.volume_change_uL == -20

# EAFP / validation
try:
    t1.add_volume(0)
    raise AssertionError("expected ValueError for zero add")
except ValueError:
    pass

# Invariant: cannot go negative
try:
    t1.consume_volume(1000)
    raise AssertionError("expected InsufficientVolumeError")
except InsufficientVolumeError:
    pass

# Transfer between tubes
t2 = SampleTube("DNA_B")
c_evt, a_evt = t1.transfer_to(t2, 50)
assert t1.volume_uL == 50 and t2.volume_uL == 50
assert c_evt.volume_change_uL == -50 and a_evt.volume_change_uL == 50
# Read-only events
evts = t1.events()
assert isinstance(evts, tuple) and len(evts) >= 3
print("All self-checks passed ✅")
