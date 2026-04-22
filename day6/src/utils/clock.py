import asyncio
import time

async def create_clock():
    while True:
        print(time.strftime("%H:%M:%S", time.localtime()))
        """
        pause the execution of the current tasks for 1 second
        """
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(create_clock())