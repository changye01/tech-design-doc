# Changye Skills Collection

一组实用的 Claude Code Skills 集合。

## 安装全部 Skills

```bash
npx skills add changye01/tech-design-doc -y -g
```

## 包含的 Skills

### 1. tech-design-doc

技术设计文档生成工具，通过引导式提问生成完整的 Markdown 格式设计文档。

**触发方式：**
- 输入 `/tech-design-doc`
- 或说"写设计文档"、"技术方案"

**功能：**
- 引导式提问，逐步完善设计文档
- 自动生成包含背景、方案设计、接口定义、实现计划的完整文档
- 内置验证脚本检查文档完整性

---

## 项目结构

```
skills/
├── tech-design-doc/           # 技术设计文档 Skill
│   ├── SKILL.md
│   ├── scripts/
│   │   └── validate_doc.py
│   ├── references/
│   │   ├── writing-guide.md
│   │   └── checklist.md
│   └── assets/
│       ├── template.md
│       └── example.md
└── [future-skill]/            # 未来可添加更多 Skills
```

## 添加新 Skill

1. 在 `skills/` 目录下创建新目录
2. 添加 `SKILL.md` 文件（必需）
3. 根据需要添加 scripts/、references/、assets/
4. 提交并推送

## 许可

MIT
