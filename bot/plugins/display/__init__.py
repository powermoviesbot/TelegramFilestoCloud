#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram


from hurry.filesize import size
from bot.plugins.display.time import time_data
import time


async def progress(current, total, up_msg, message, start_time):

    time_now = time.time()
    time_diff = time_now - start_time
    percent = round(current * 100 // total)
    progress_ = "{0} {1}%".format(
        progressBar(percent),
                percent
    )
    time_ = "Time: {0}".format(
        time_data(start_time)
    )

    speed_ = "Speed: {0}".format(
        size(current / time_diff)
    )
    download_ = "{0} of {1}".format(
        size(current),
        size(total)
    )
    try:

        await message.edit(
            text=f"{progress_}\n{download_}\n{speed_}    {time_}"
        )

    except Exception as e:
        await message.edit(
            text=f"ERROR: {e}"
        )


def progressBar(percent):
    done_block = '█'
    empty_block = '░'
    return f"{done_block * int(percent / 5)}{empty_block * int(20 - int(percent / 5))}"
