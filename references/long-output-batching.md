# Long Output Batching

Use this protocol for full manuscripts or any output likely to exceed a few thousand words. Do not generate the entire `英文全文成稿.md` or `翻译审校说明.md` in one response or one large file write.

## Default Directory Layout

Create a task-specific folder:

```text
translation_work/<source-stem>/
├─ translation_units.json
├─ structure_map.md
├─ batch_manifest.md
├─ draft_parts/
│  ├─ 01_abstract.md
│  ├─ 02_introduction.md
│  ├─ 03_results.md
│  ├─ 04_methods.md
│  └─ ...
├─ review_parts/
│  ├─ 01_abstract_review.md
│  ├─ 02_introduction_review.md
│  ├─ 03_results_review.md
│  ├─ 04_methods_review.md
│  └─ ...
├─ 英文全文成稿.md
├─ 翻译审校说明.md
└─ coverage_audit.md
```

## Batch Manifest

Before generating full outputs, write `batch_manifest.md` with:

- batch ID
- section name
- source unit ID range
- output draft part path
- output review part path
- status: `pending`, `in_progress`, `done`, or `needs_revision`
- notes on formulas, tables, figures, or units needing review

Update the manifest after each batch. If a network interruption occurs, resume from the first batch not marked `done`.

## Batch Size

Default batch boundaries:

- abstract as one batch
- introduction as one or more batches
- each major results subsection as one batch
- methods as one or more batches
- discussion/conclusion as one batch
- figure/table notes as separate small batches when numerous

Keep each batch small enough to finish safely in one response. Prefer 800-1,500 English words per batch, or fewer for technically dense methods/results sections.

## Generation Protocol

For each batch:

1. Read only the source units for that batch plus the current terminology table and style cards.
2. Generate the draft part file in `draft_parts/`.
3. Generate the matching review part file in `review_parts/`.
4. Check that all source unit IDs in the batch appear in either the draft part or review part.
5. Update `batch_manifest.md` to `done`.
6. Continue to the next batch.

Do not start by writing `英文全文成稿.md` directly. Full files are assembled only after all parts are marked `done`.

## Assembly Protocol

After all batches are done:

1. Concatenate `draft_parts/*.md` in manifest order into `英文全文成稿.md`.
2. Concatenate `review_parts/*.md` in manifest order into `翻译审校说明.md`.
3. Run coverage audit when `translation_units.json` is available.
4. If audit fails, fix only the affected batch part, then reassemble.

## Interruption Recovery

If output generation is interrupted:

- Do not restart the whole manuscript.
- Read `batch_manifest.md`.
- Verify the last `in_progress` part file is complete.
- If incomplete, rewrite only that batch part.
- Resume from the first batch whose status is not `done`.

## User-Facing Status

After every 1-3 batches, report compact progress:

```text
Completed: 03_results.md
Next: 04_methods.md
Remaining: 2 batches
Issues: S12-P004 needs formula review
```

Avoid long progress narration that competes with translation context.
