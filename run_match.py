"""可选的完整对局功能检查；对手为内置代理，不是排名评估。"""
import argparse
import contextlib
import importlib.metadata
import io
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, default=20261015)
    parser.add_argument('--opponent', choices=['random', 'starter', 'pass'], default='random')
    parser.add_argument('--output', type=Path, default=Path('new_results/smoke_check.json'))
    args = parser.parse_args()
    if importlib.metadata.version('kaggle-environments') != '1.32.7':
        raise RuntimeError('该历史引擎检查需要 kaggle-environments==1.32.7。')
    if args.output.exists():
        raise FileExistsError('请选择新输出路径，不覆盖已有结果。')
    # 隐藏环境注册日志，避免结果摘要出现大量无关内容。
    with contextlib.redirect_stdout(io.StringIO()):
        from kaggle_environments import make
        from kaggle_environments.agent import get_last_callable
        source_path = Path(__file__).resolve().parent / 'main.py'
        entry = get_last_callable(source_path.read_text(encoding='utf-8'), path=str(source_path))
        env = make('kaggriculture', configuration={'episodeSteps': 720, 'seed': args.seed}, debug=True)
        env.run([entry, args.opponent])
    final = env.steps[-1]
    diagnostics = dict(getattr(entry, 'telemetry', {}))
    result = {
        'purpose': '功能执行检查，不是竞技实力估计。',
        'engine': '1.32.7', 'seed': args.seed, 'opponent': args.opponent,
        'status': [str(state.status) for state in final],
        'money': [int(farm['money']) for farm in final[0].observation['farms']],
        'calls': diagnostics.get('calls'), 'diagnostics': diagnostics,
    }
    assert all(state == 'DONE' for state in result['status'])
    assert result['calls'] == 719 and diagnostics.get('errors', 0) == 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
