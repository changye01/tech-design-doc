# tech-design-doc Skill

技术设计文档生成工具，通过引导式提问生成完整的 Markdown 格式设计文档。

## 安装

### 方式 1：npx（推荐）

```bash
npx add-skill changye01/tech-design-doc
```

### 方式 2：手动克隆

```bash
# 全局安装（所有项目可用）
git clone git@github.com:changye01/tech-design-doc.git ~/.claude/skills/tech-design-doc

# 或项目级安装
git clone git@github.com:changye01/tech-design-doc.git .claude/skills/tech-design-doc
```

## 使用

安装后在 Claude Code 中：

- 输入 `/tech-design-doc` 触发
- 或在对话中说"写设计文档"、"技术方案"、"TDD"

## 功能

- 引导式提问，逐步完善设计文档
- 自动生成包含背景、方案设计、接口定义、实现计划的完整文档
- 内置验证脚本检查文档完整性

## 包含内容

```
tech-design-doc/
├── SKILL.md                 # 工作流程和引导问题
├── scripts/
│   └── validate_doc.py      # 文档完整性验证脚本
├── references/
│   ├── writing-guide.md     # 写作指南
│   └── checklist.md         # 自检清单
└── assets/
    ├── template.md          # 文档模板
    └── example.md           # 完整示例
```

## 许可

MIT
