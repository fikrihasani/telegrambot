import asyncio
import telegram


async def main():
    bot = telegram.Bot("7257981613:AAGG5XuQV3jF-H3E3PyZS1ypXHh4Zt8eCuc")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())