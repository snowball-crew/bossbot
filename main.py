from bossbot.controller.discord_controller import DiscordController
from bossbot.domain.bossbot import BossBot
from bossbot.repository.commute_clock_repository import CommuteClockRepository
from bossbot.service.commute_service import CommuteService

bossbot = BossBot()

commute_clock_repository = CommuteClockRepository()
commute_service = CommuteService(commute_clock_repository)
discord_controller = DiscordController(bossbot, commute_service)


discord_controller.run()
