from os import getenv

from dotenv import load_dotenv

x = load_dotenv()
if x:
    API_ID = int(getenv("API_ID", None))
    API_HASH = getenv("API_HASH", None)
else:
    API_ID = input("\nEnter Your API_ID:\n > ")
    API_HASH = input("\nEnter Your API_HASH:\n > ")

import asyncio

from pyrogram import Client as c
print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")


asyncio.run(main())
