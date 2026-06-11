# Section Translation Profiles

Use these profiles to prevent sentence-by-sentence literalism. Sentence-level translation is an internal coverage mechanism. The final English draft should follow the target section's rhetorical function.

## Core Rule

Do not preserve Chinese sentence count, clause order, or enumeration density when they make the English draft verbose. Preserve source meaning, evidence, claim strength, and all material results.

Use `readability-rules.md` together with these profiles. Section-level synthesis should not produce long, clause-heavy English sentences.

When compressing, record the decision in `翻译审校说明.md` so the user can verify that no material point was lost.

## Abstract Profile

Default mode: concise synthesis.

Aim for the target journal's abstract length and density. If no target rule is known, prefer a compact 180-250 word abstract for long Chinese abstracts and avoid turning every Chinese sentence into one English sentence.

Keep abstract sentences especially readable. Prefer several short sentences over one dense sentence that combines data, method, result, and implication.

Include:

- broad motivation or research tension
- data and empirical design
- main effect
- most important mechanism or channel
- key heterogeneity or boundary condition only if central
- cost-benefit or counterfactual result only if central to contribution
- final implication

Compress:

- long "first, second, third..." lists into thematic result clusters
- repeated policy framing
- multiple subgroup findings into one sentence when they support the same point
- detailed numeric secondary results unless they are central

Avoid:

- reproducing every numbered finding as a separate English sentence
- long chains of "whereas", "while", and "respectively" if they overload the abstract
- methods-level detail that belongs in the Methods or Results sections
- adding a stronger contribution claim than the source supports

Recommended abstract movement:

1. Problem and empirical gap.
2. Data and identification.
3. Main finding plus spatial or substantive magnitude.
4. Mechanism and key boundary conditions.
5. Welfare/counterfactual implication if central.
6. Final contribution or policy implication.

## Introduction Profile

Use clearer narrative progression than the Chinese source when needed, but do not change the evidence chain:

1. general problem
2. unresolved tension or empirical gap
3. why the setting/data identify the question
4. core design and findings
5. contribution and implication

Compress background repetition. Preserve all claims that define the paper's contribution.

## Results Profile

Default mode: faithful but readable.

Results sections can be more granular than abstracts. Preserve the sequence of empirical claims, but combine sentences when English would otherwise sound like a table-by-table report.

Do not combine too many results into one sentence. If a sentence reports a main effect, subgroup contrast, mechanism, and robustness claim together, split it.

Use result-first sentences:

- State the substantive finding.
- Then state the estimate, comparison, or test.
- Then explain interpretation or boundary.

## Methods Profile

Default mode: precise translation.

Use less compression than abstracts. Preserve definitions, model structure, variable construction, sample restrictions, and identification assumptions. Do not simplify technical meaning for style.

Even in methods, avoid long sentences that define several variables or sample restrictions at once. Split definitions across sentences when precision is maintained.

## Discussion Profile

Default mode: concise interpretation.

Compress repeated result summaries. Preserve limitations, policy boundaries, and causal caution. Do not broaden recommendations beyond the source.

## Compression Notes

When final prose condenses source sentences, add a compact note:

```markdown
### S02-P003

- Section: Abstract
- Compression decision: Consolidated five numbered findings into three thematic result sentences.
- Coverage retained: main effect, spatial decay, species decomposition, mechanism, boundary conditions, welfare comparison, counterfactual siting.
- Material details omitted from abstract draft: none / <list details moved out because they are secondary>.
```
