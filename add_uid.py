import json
import os

# 动态 ID 存储文件
ID_FILE = "dynamic_ids.json"

# 读取已保存的动态 ID
def load_dynamic_ids():
    if os.path.exists(ID_FILE):
        with open(ID_FILE, "r") as file:
            return json.load(file)
    return {}

# 保存最新的动态 ID
def save_dynamic_ids(dynamic_ids):
    with open(ID_FILE, "w") as file:
        json.dump(dynamic_ids, file, indent=4)

# 添加新用户 UID
def add_new_uid(new_uid):
    dynamic_ids = load_dynamic_ids()

    if str(new_uid) not in dynamic_ids:
        dynamic_ids[str(new_uid)] = None  # 初始化动态 ID 为 None
        save_dynamic_ids(dynamic_ids)
        print(f"✅ 成功添加新 UID:{new_uid}")
    else:
        print(f"⚠️ UID {new_uid} 已存在，无需重复添加。")

# 删除用户 UID
def remove_uid(uid):
    dynamic_ids = load_dynamic_ids()

    if str(uid) in dynamic_ids:
        del dynamic_ids[str(uid)]
        save_dynamic_ids(dynamic_ids)
        print(f"✅ 成功删除 UID：{uid}")
    else:
        print(f"❌ UID {uid} 不存在，无法删除。")

# 展示当前监测的所有 UID
def list_uids():
    dynamic_ids = load_dynamic_ids()
    if dynamic_ids:
        print("📋 当前监测的 UID 列表：")
        for uid in dynamic_ids:
            print(f"- {uid}")
    else:
        print("📭 当前没有监测的 UID。")

# 命令行交互
def main():
    print("=== B站 UID 管理工具 ===")
    print("1. 添加 UID")
    print("2. 删除 UID")
    print("3. 查看所有 UID")
    print("4. 退出")

    while True:
        choice = input("\n请输入操作选项 (1/2/3/4):")

        if choice == "1":
            new_uid = input("请输入要添加的 UID:")
            if new_uid.isdigit():
                add_new_uid(int(new_uid))
            else:
                print("❌ UID 应为数字。")
        elif choice == "2":
            uid = input("请输入要删除的 UID:")
            if uid.isdigit():
                remove_uid(int(uid))
            else:
                print("❌ UID 应为数字。")
        elif choice == "3":
            list_uids()
        elif choice == "4":
            print("👋 已退出 UID 管理工具。")
            break
        else:
            print("❗ 无效选项，请重新输入。")

if __name__ == "__main__":
    main()
