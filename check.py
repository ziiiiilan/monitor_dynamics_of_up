import json
import os
from bilibili_api import user, sync


# 动态 ID 存储文件
ID_FILE = "dynamic_ids.json"

# 读取已保存的动态 ID
def load_dynamic_ids():
    if os.path.exists(ID_FILE):
        with open(ID_FILE, "r") as file:
            return json.load(file)
    return {}  # 如果文件不存在，返回空字典

# 保存最新的动态 ID
def save_dynamic_ids(dynamic_ids):
    with open(ID_FILE, "w") as file:
        json.dump(dynamic_ids, fp=file, indent=4)

# 检测单个用户是否有新动态
async def check_user_dynamics(uid, dynamic_ids,results):
    u = user.User(uid=uid)
    last_dynamic_id = dynamic_ids.get(str(uid))  # 获取上次记录的动态 ID

    try:
        # 获取最新一页动态
        page = await u.get_dynamics_new()
        if page["items"]:
            new_dynamic_id = page["items"][0]["id_str"]

            if last_dynamic_id is None:
                # 第一次记录
                dynamic_ids[str(uid)] = new_dynamic_id
                results.append(f"https://space.bilibili.com/{uid} 首次记录最新动态 ID: {new_dynamic_id}\n")
            elif new_dynamic_id != last_dynamic_id:
                # 检测到新动态
                results.append(f"https://space.bilibili.com/{uid} 检测到新动态！🎉 新动态 ID: {new_dynamic_id}\n")
                dynamic_ids[str(uid)] = new_dynamic_id
            else:
                results.append(f"https://space.bilibili.com/{uid} 暂无新动态。\n")
        else:
            results.append(f"https://space.bilibili.com/{uid} 未找到动态。\n")

    except Exception as e:
        results.append(f"[UID: {uid}] 检测失败，错误信息：{e}\n")

def save_results_to_file(results):
    filename = "check_results.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(results)

    print(f"✅ 检测结果已保存至 {filename}")


# 主函数，遍历所有用户
async def main():
    results=[]
    dynamic_ids = load_dynamic_ids()
    uids=dynamic_ids.keys()
    for uid in uids:
        await check_user_dynamics(uid, dynamic_ids,results=results)

    save_dynamic_ids(dynamic_ids)
    save_results_to_file(results=results)

# 入口
sync(main())
