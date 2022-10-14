from machine import Pin
from time import sleep, time
from hcsr04 import HCSR04

import uasyncio as asyncio
import gc, dht

# ============================================================================

gc.collect()
gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

# ============================================================================

sensor = dht.DHT22(Pin(14))
sonic = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)

# ============================================================================

async def Temperature():
    while True:
        try:
            sensor.measure()
            temp = sensor.temperature()
            hum = sensor.humidity()
            temp_f = temp * (9/5) + 32.0
            print("Temperature: %3.1f C" %temp)
            print("Temperature: %3.1f F:" %temp_f)
            print("Humidity: %3.1f %%" %hum)
            print()
            await asyncio.sleep(1) # Pause 1s
        except OSError as e:
            print("Failed to read sensor.")
         
async def UltraSonic():
    while True:
        try:
            distance = sonic.distance_cm()
            print('Distance:', distance, 'cm')
            print()
            await asyncio.sleep(1) # Pause 1s
        except OSError as e:
            print("Failed to read sensor.")

# ============================================================================

async def main():
    asyncio.create_task(Temperature())
    asyncio.create_task(UltraSonic())
    await asyncio.sleep(10)
    
# ============================================================================
if __name__ == "__main__":
    s = time()
    asyncio.run(main())
    elapsed = time() - s
    print(f"Executed in {elapsed:0.2f} seconds.")
# ============================================================================