from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..SubscriberManager import SubscriberManager


class BaseSubscriber:
    def __init__(self, id: int, manager: 'SubscriberManager'):
        self.flag    = None
        self.id      = id
        # ---
        self.manager = manager       # 管理オブジェクトの参照を保持
        self.manager.register(self)  # 管理オブジェクトに自分を登録

    def update_flag(self):
        self.flag = True
        self.manager.update_state(self.id, self.flag)  # 状態更新を通知
