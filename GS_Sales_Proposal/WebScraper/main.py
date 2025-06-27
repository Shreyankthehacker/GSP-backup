import asyncio
from scrape import get_data
async def main():
    result = await get_data('https://www.whatsapp.com/')
    print(result.extracted_content)

if __name__ == '__main__':
    asyncio.run(main())
