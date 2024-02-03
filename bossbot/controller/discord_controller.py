from discord import Member, VoiceState
from discord.ext.commands import Bot

from bossbot.service.commute_service import CommuteService


class DiscordController:
    MOGAKKO_CHANNEL_NAME: str = "온라인모각코2"
    ALERT_CHANNEL_NAME: str = "온라인모각코2"

    def __init__(self, discord_bot: Bot, commute_service: CommuteService):
        self.discord_bot = discord_bot
        self.commute_service = commute_service

        self.discord_bot.event(self.on_ready)
        self.discord_bot.event(self.on_voice_state_update)

    async def on_ready(self) -> None:
        print(f"Logged in as {self.discord_bot.user.name} ({self.discord_bot.user.id})")

    async def on_voice_state_update(
        self,
        member: Member,
        before: VoiceState,
        after: VoiceState,
    ):
        """
        출퇴근 시 알림을 보냅니다.

        # TODO : 이벤트 이름을 변경할 수 있는지 확인, 가독성 좋은 이름으로 변경
        """
        if self._check_entered_mogakko_channel(after):
            await self._alert_commute_on(member, after)
        elif self._check_left_mogakko_channel(before):
            await self._alert_commute_off(member, before)

    def run(self, *args, **kwargs):
        self.discord_bot.run(*args, **kwargs)

    async def _alert_commute_on(
        self,
        member: Member,
        before: VoiceState,
    ):
        await self.commute_service.alert_commute_on(member, before)

    async def _alert_commute_off(
        self,
        member: Member,
        before: VoiceState,
    ) -> None:
        await self.commute_service.alert_commute_off(member, before)

    def _check_entered_mogakko_channel(self, after):
        return (
            after.channel is not None
            and self.MOGAKKO_CHANNEL_NAME in after.channel.name
        )

    def _check_left_mogakko_channel(self, before):
        return (
            before.channel is not None
            and self.MOGAKKO_CHANNEL_NAME in before.channel.name
        )
