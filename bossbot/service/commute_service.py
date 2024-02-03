from discord.utils import get

from bossbot.repository.base import Repository


class CommuteService:
    MOGAKKO_CHANNEL_NAME: str = "온라인모각코2"
    # ALERT_CHANNEL_NAME: str = "✅-모각코-출석부"
    ALERT_CHANNEL_NAME: str = "온라인모각코2"

    def __init__(self, commute_repository: Repository):
        self.commute_repository = commute_repository

    async def alert_commute_on(self, member, after) -> None:
        alert_channel = self._get_alert_channel(after.channel.guild)
        await alert_channel.send(
            f"{member.name}님이 {after.channel.name} 에 출근하셨습니다!"
        )

    async def alert_commute_off(self, member, before):
        alert_channel = self._get_alert_channel(before.channel.guild)
        await alert_channel.send(
            f"{member.name}님이 {before.channel.name} 에서 퇴근하셨습니다!"
        )

    def _get_alert_channel(self, guild):
        alert_channel = get(guild.channels, name=self.ALERT_CHANNEL_NAME)

        if alert_channel is None:
            raise ValueError(f"채널 {self.ALERT_CHANNEL_NAME}이 없습니다.")

        return alert_channel
