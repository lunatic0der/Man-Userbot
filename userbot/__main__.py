# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
""" Userbot start point """

import sys
from importlib import import_module

from pytgcalls import idle
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import ALIVE_NAME, BOT_VER, BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import (
    LOGS,
    MAN2,
    MAN3,
    MAN4,
    MAN5,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    UPSTREAM_REPO_BRANCH,
    bot,
    call_py,
)
from userbot.modules import ALL_MODULES
from userbot.utils import checking

INVALID_PH = (
    "\nERROR: Nomor Telepon yang kamu masukkan SALAH."
    "\nTips: Gunakan Kode Negara beserta nomornya atau periksa nomor telepon Anda dan coba lagi."
)


# Multi-Client helper
async def man_client(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)


# Multi-Client Starter
def multiman():
    failed = 0
    if STRING_2:
        LOGS.info("STRING_2 detected! Starting 2nd Client.")
        try:
            MAN2.start()
            MAN2.loop.run_until_complete(man_client(MAN2))
        except:
            LOGS.info("STRING_2 failed. Please Check Your String session.")
            failed += 1

    if STRING_3:
        LOGS.info("STRING_3 detected! Starting 3rd Client.")
        try:
            MAN3.start()
            MAN3.loop.run_until_complete(man_client(MAN3))
        except:
            LOGS.info("STRING_3 failed. Please Check Your String session.")
            failed += 1

    if STRING_4:
        LOGS.info("STRING_4 detected! Starting 4th Client.")
        try:
            MAN4.start()
            MAN4.loop.run_until_complete(man_client(MAN4))
        except:
            LOGS.info("STRING_4 failed. Please Check Your String session.")
            failed += 1

    if STRING_5:
        LOGS.info("STRING_5 detected! Starting 5th Client.")
        try:
            MAN5.start()
            MAN5.loop.run_until_complete(man_client(MAN5))
        except:
            LOGS.info("STRING_5 failed. Please Check Your String session.")
            failed += 1

    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    return failed


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.start()
        call_py.start()
        failed_client = multiman()
        global total
        total = 5 - failed_client
        LOGS.info(f"» Total Clients = {total} «")
    except Exception as e:
        LOGS.error(f'{e}')
        sys.exit()


for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Jika {ALIVE_NAME} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/SharingUserbot"
)

LOGS.info(f"Man-Userbot ⚙️ V{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")


async def man_userbot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"🔥 **Man-Userbot Berhasil Di Aktifkan**\n━━\n➠ **Userbot Version -** `{BOT_VER}@{UPSTREAM_REPO_BRANCH}`\n➠ **Ketik** `{cmd}alive` **untuk Mengecheck Bot**\n━━",
            )
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(JoinChannelRequest("@Lunatic0de"))
        await bot(JoinChannelRequest("@SharingUserbot"))
    except BaseException:
        pass


bot.loop.create_task(checking())
bot.loop.create_task(man_userbot_on())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
