#!/usr/bin/env python3
"""
时间冲突检测器 — 刘亚格十一假期模式
检测多个时间任务是否有重叠，并给出错峰建议

用法: python3 conflict-detector.py < tasks.yaml
"""

import json
import sys
from datetime import datetime, timedelta


def parse_time_range(s):
    """解析时间范围，支持 '2026-10-01' 或 '2026-10-01~2026-10-03' 格式"""
    if not s or not isinstance(s, str):
        return None, None
    s = s.strip()
    if "~" in s:
        parts = s.split("~")
        try:
            start = datetime.strptime(parts[0].strip(), "%Y-%m-%d")
            end = datetime.strptime(parts[1].strip(), "%Y-%m-%d")
            if start == end:
                end = end + timedelta(days=1)  # 同一天 = 当天全天
            return start, end
        except ValueError:
            return None, None
    if "-" in s and s.count("-") >= 2:
        parts = s.split()
        if len(parts) == 1:
            try:
                d = datetime.strptime(s, "%Y-%m-%d")
                return d, d + timedelta(days=1)
            except ValueError:
                return None, None
        try:
            return datetime.strptime(s, "%Y-%m-%d %H:%M"), None
        except ValueError:
            return None, None
    return None, None


def detect_conflicts(tasks):
    """检测任务之间的时间冲突"""
    parsed = []
    for task in tasks:
        name = task.get("name", task.get("男友", "未知"))
        time_str = task.get("time", task.get("时间", ""))
        desc = task.get("desc", task.get("描述", ""))
        start, end = parse_time_range(time_str)
        if start and not end:
            end = start + timedelta(days=1)
        parsed.append((name, start, end, desc))

    conflicts = []
    for i in range(len(parsed)):
        for j in range(i + 1, len(parsed)):
            n1, s1, e1, d1 = parsed[i]
            n2, s2, e2, d2 = parsed[j]
            if s1 and s2 and e1 and e2:
                # 判断重叠
                overlap_start = max(s1, s2)
                overlap_end = min(e1, e2)
                if overlap_start < overlap_end:
                    conflicts.append(
                        {
                            "tasks": [n1, n2],
                            "overlap_start": overlap_start.strftime("%m-%d %H:%M"),
                            "overlap_end": overlap_end.strftime("%m-%d %H:%M"),
                            "severity": "高" if (overlap_end - overlap_start).seconds > 3600 else "中",
                        }
                    )

    return conflicts


def suggest_rebalance(tasks, conflicts):
    """给出错峰建议"""
    suggestions = []
    for c in conflicts:
        t1, t2 = c["tasks"]
        suggestions.append(
            f"⚠️ [{c['severity']}] {t1} ↔ {t2} 在 {c['overlap_start']}~{c['overlap_end']} 冲突！"
        )
        suggestions.append(
            f"   → 建议：{t1} 提前到上午，{t2} 改到下午，或交换其中一天"
        )
    if not suggestions:
        suggestions.append("✅ 完美！所有任务时间线无重叠，刘亚格看了都说好。")
    return suggestions


def main():
    tasks = [
        {"name": "男友A", "time": "2026-09-28~2026-09-30", "desc": "同居"},
        {"name": "男友B", "time": "2026-10-01~2026-10-03", "desc": "旅游"},
        {"name": "男友C", "time": "2026-10-04~2026-10-06", "desc": "见家长+旅游"},
    ]

    if len(sys.argv) > 1 and sys.argv[1] == "--conflict-demo":
        # 有冲突的示例
        tasks = [
            {"name": "数据库备份", "time": "2026-06-01~2026-06-01", "desc": "每天 9:00 开始，约 20 分钟"},
            {"name": "日报生成", "time": "2026-06-01~2026-06-01", "desc": "每天 9:00 开始，约 10 分钟"},
            {"name": "周会提醒", "time": "2026-06-02~2026-06-02", "desc": "周二 9:30"},
        ]
    elif len(sys.argv) > 1 and sys.argv[1] == "--demo":
        pass  # 使用默认示例（无冲突）
    elif not sys.stdin.isatty():
        import yaml

        try:
            data = yaml.safe_load(sys.stdin)
            if data and "tasks" in data:
                tasks = data["tasks"]
        except ImportError:
            print("⚠️ 建议安装 PyYAML: pip install pyyaml")
            try:
                tasks = json.load(sys.stdin)
                if isinstance(tasks, dict) and "tasks" in tasks:
                    tasks = tasks["tasks"]
            except json.JSONDecodeError:
                print("⚠️ 输入不是 JSON，使用默认示例")

    print("═" * 50)
    print("  ⏰ 时间冲突检测器 — 刘亚格十一假期模式")
    print("═" * 50)

    for t in tasks:
        print(f"  [{t['name']}] {t['time']} — {t.get('desc', '')}")

    print()
    conflicts = detect_conflicts(tasks)
    suggestions = suggest_rebalance(tasks, conflicts)

    for s in suggestions:
        print(f"  {s}")

    print("═" * 50)


if __name__ == "__main__":
    main()
