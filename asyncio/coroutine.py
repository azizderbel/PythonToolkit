import asyncio

async def square(number: int) -> int:
    return number*number # return a coroutine object

"""result = square(10)
print(result)"""

# to run coroutines, you need to execute it on an event loop
result = asyncio.run(square(10))
print(result)
print('user')
