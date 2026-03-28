"""
title: Example Filter
author: open-webui
author_url: https://github.com/open-webui
funding_url: https://github.com/open-webui
version: 0.1
"""

# pydantic 用來定義資料模型與驗證欄位
from pydantic import BaseModel, Field
from typing import Optional


class Filter:
    """
    Filter 是 Open WebUI 的過濾器插件類別。
    它會在每次對話請求「進入」和「離開」API 時被呼叫，
    可以用來檢查、修改或限制對話內容。
    """

    class Valves(BaseModel):
        """
        Valves 是管理員層級的設定，由系統管理員配置。
        這些設定會影響所有使用者。
        """
        priority: int = Field(
            default=0, description="過濾器的優先順序，數字越小越先執行。"
        )
        max_turns: int = Field(
            default=8, description="系統允許的最大對話輪數上限（管理員設定）。"
        )
        pass

    class UserValves(BaseModel):
        """
        UserValves 是使用者層級的設定，每個使用者可以自行調整。
        """
        max_turns: int = Field(
            default=4, description="使用者自己設定的最大對話輪數。"
        )
        pass

    def __init__(self):
        # 若要啟用自訂檔案處理邏輯，可取消下方註解。
        # 啟用後，WebUI 會將檔案相關操作交由此類別的方法處理，
        # 而不使用預設的檔案處理流程。
        # self.file_handler = True

        # 初始化 valves，載入管理員層級的預設設定。
        self.valves = self.Valves()
        pass

    def inlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        # 我要取得使用者輸入的內容
        print("使用者輸入\n")

        return body  # 回傳（可能已修改的）請求內容

    def outlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        """
        outlet 是「出口」處理函式，在 AI 模型回應之後被呼叫。
        可以在這裡對回應進行分析、記錄或修改。

        參數:
            body: AI 模型回應的內容。
            __user__: 目前使用者的資訊。

        回傳:
            修改後（或原始）的 body 字典。
        """
        print("模型輸出\n","*"*30,"\n")

        return body  # 回傳（可能已修改的）回應內容
