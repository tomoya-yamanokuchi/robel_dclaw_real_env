# robel_dclaw_real_env


## 概要
- simulation envと対を成すrealのenvコードです

---
## 事前設定

### 関連パッケージのインストール

- 以下の関連するパッケージを本リポジトリと同一階層にクローンしてくる

```
git clone https://github.com/tomoya-yamanokuchi/robel_dclaw_task_space.git
git clone https://github.com/tomoya-yamanokuchi/robel_dclaw_ros.git
git clone https://github.com/tomoya-yamanokuchi/robel_dclaw_kinematics.git
git clone https://github.com/tomoya-yamanokuchi/angle_interface.git
git clone https://github.com/tomoya-yamanokuchi/dynamixel_ros_service.git
```

- `setup.py`を作成して、まとめてパッケージをインストールできるようにする
- 以下は例です

```python
from setuptools import setup, find_packages

setup(
    name='robel_dclaw_real_experiment', # パッケージ名
    version='0.1',                      # バージョン番号
    packages=find_packages(),           # パッケージを自動的に探してインクルード
)
```

- 同じ階層で、上記で作成した`setup.py`を用いてpip installして関連をパッケージをインストール
- pythonは実行環境に合わせてください
- パッケージを編集可能にするために`-e`のオプションをつけてください
```
python -m pip install -e .
```

---
## テストコードを実行

例：
```
python3.7 -m robel_dclaw_real_env.test.test_env_get_state_check      # 状態オブジェクトの確認
python3.7 -m robel_dclaw_real_env.test.test_env_get_state_loop       # 状態取得のループを回す
python3.7 -m robel_dclaw_real_env.test.test_env_reset_case1          # 特定の初期状態にリセット
python3.7 -m robel_dclaw_real_env.test.test_env_reset_case2　　      # 別の初期状態にリセット
python3.7 -m robel_dclaw_real_env.test.test_env_valve_rotation_plus  # タスクスペースで値を一定値プラスしながら指を動かす
python3.7 -m robel_dclaw_real_env.test.test_env_valve_rotation_minus # タスクスペースで値を一定値マイナスしながら指を動かす
```

## envのユースケースの例

- `test_env_valve_rotation_minus.py`の例です
- 基本的にはsimのenvと共通したインターフェースで使えるようにしています

```python
from sqlite3 import paramstyle
import numpy as np
from .. import RobelDClawValveRealEnvironment
from robel_dclaw_task_space.value_object import Manifold1D
from robel_dclaw_ros.utils import ParameterObject


def run_tests():
    # ----
    task_space_position_init = np.array([0.65, 0.18, 0.65])
    task_space_ctrl_init     = Manifold1D(value=task_space_position_init.reshape(1,1,3))
    # ----
    params = ParameterObject()
    params.sleep_time_sec = 0.1
    env = RobelDClawValveRealEnvironment(params)
    env.reset(task_space_ctrl_init)
    # ----
    num_step = 100
    task_space_ctrl = task_space_ctrl_init
    for i in range(num_step):
        task_space_ctrl.value += 0.01
        env.set_ctrl_task_sapce(task_space_ctrl)
        env.step()

if __name__ == "__main__":
    run_tests()
```
