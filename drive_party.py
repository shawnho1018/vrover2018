
##Import local library explore: see explore.py
import gpio_cleanup
import explore

print("\n\nStarting Test: drive_party\n\n")

for z in range(20):
    explore.mode_discovery(2, 0.03, 'party', 'on')

print("\n\nFinished drive_party\n\nrun me again!")
