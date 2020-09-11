import discord
from discord.ext import commands
from utils.basecog import BaseCog
from utils.embedmgr import aEmbedBase


class Canceled(aEmbedBase):
    async def ko(self):
        embed = discord.Embed(title="❌ 취소되었습니다.", color=self.cog.color["error"])
        return embed

    async def en(self):
        embed = discord.Embed(title="❌ Canceled.", color=self.cog.color["error"])
        return embed


class MissingArgs(aEmbedBase):
    async def ko(self, paramdesc):
        return discord.Embed(
            title="❗ 명령어에 빠진 부분이 있습니다!",
            description=f"**`{paramdesc}`이(가) 필요합니다!**\n자세한 명령어 사용법은 `{self.cog.prefix}도움` 을 통해 확인하세요!",
            color=self.cog.color["error"],
        )


class CharNotFound(aEmbedBase):
    async def ko(self, charname):
        return discord.Embed(
            title=f"❓ 존재하지 않는 캐릭터입니다!: `{charname}`", color=self.cog.color["error"]
        )


class NotEnoughMoney(aEmbedBase):
    async def ko(self, more_required: int):
        return discord.Embed(
            title="❓ 돈이 부족합니다!",
            description=f"`{more_required}`골드가 부족합니다!",
            color=self.cog.color["error"],
        )


class SubcommandNotFound(aEmbedBase):
    async def ko(self):
        return discord.Embed(
            title="❓ 존재하지 않는 하위 명령어입니다!",
            description="""\
                사용할 수 있는 하위 명령어들:
                {}{} [{}]
            """.format(
                self.cog.prefix,
                self.ctx.command.name,
                "/".join(map(lambda x: x.name, self.ctx.command.commands))
            ),
        )