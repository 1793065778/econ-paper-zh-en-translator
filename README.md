# Econ Paper ZH-EN Translator

A Codex skill for translating Chinese economics, management, finance, policy evaluation, environmental/resource economics, and empirical social-science manuscripts into English academic paper drafts.

This skill is designed for full manuscript translation, not isolated paragraph-by-paragraph machine translation. It decomposes a manuscript, tracks terminology and variables, adapts expression to target-journal examples, and generates reviewable English drafts in batches.

## Why This Skill

Traditional AI translation often struggles with long academic manuscripts:

- key terms and acronyms drift across sections;
- variables are translated inconsistently;
- target journal style is not reflected;
- long Chinese sentences become long, hard-to-read English sentences;
- large one-shot outputs fail or lose context;
- missing paragraphs are hard to detect.

This skill addresses those problems through a structured translation workflow.

## Highlights

- **Context consistency**: builds and updates terminology, acronym, and variable tables across the manuscript.
- **Target-journal adaptation**: learns transferable expression patterns from user-provided or AI-found target-journal examples.
- **Coverage control**: uses DOCX extraction and paragraph IDs to reduce omission risk.
- **Readable academic English**: treats sentence-level translation as an internal coverage check, then rewrites for clear English prose.
- **Section-aware translation**: abstracts are compressed and synthesized; methods stay precise; results stay faithful but readable.
- **Batch output**: long manuscripts are translated into `draft_parts/` and `review_parts/` before final assembly, reducing failure risk.
- **Review artifacts**: produces a clean English draft plus separate translation review notes.

## Default Outputs

- `英文全文成稿.md`: clean English manuscript draft.
- `翻译审校说明.md`: terminology, compression decisions, readability revisions, questions, protected items, and coverage audit.
- Optional English replacement `.docx` after Markdown confirmation.

## Main Workflow

1. Extract DOCX units and produce a structure map.
2. Confirm translation scope.
3. Build target-journal style cards.
4. Build terminology/acronym/variable tables.
5. Produce and confirm a trial translation.
6. Translate full manuscript in batches.
7. Assemble final Markdown outputs.
8. Run coverage audit.
9. Optionally generate a DOCX version.

## Installation

Copy this folder into your Codex skills directory:

```text
C:\Users\<you>\.codex\skills\econ-paper-zh-en-translator
```

Then invoke it in Codex with:

```text
$econ-paper-zh-en-translator
```

## Notes

- This is a translation skill, not a manuscript rewriting skill.
- It preserves facts, data, coefficients, variables, identification strategy, causal strength, and policy claims.
- It does not add findings, mechanisms, robustness checks, references, or contributions.
- For Windows DOCX workflows, run scripts with UTF-8 mode, for example `python -X utf8`.
