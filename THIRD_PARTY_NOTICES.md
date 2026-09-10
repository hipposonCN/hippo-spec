# Method attribution

The bundled diagnosis and domain-modeling guidance adapts methods and format ideas from [Matt Pocock Skills](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015), revision `3cca18b368ae95cdbdebbff572ccafa662551015`:

- `skills/engineering/diagnosing-bugs/SKILL.md`
- `skills/engineering/domain-modeling/SKILL.md`
- `skills/engineering/domain-modeling/CONTEXT-FORMAT.md`
- `skills/engineering/domain-modeling/ADR-FORMAT.md`

Hippo Spec narrows their triggers, preserves the root assignment's authorization, and embeds the required guidance locally. These are adapted references, not separately invoked upstream skills. Upstream changes do not silently alter this package.

[OpenSpec](https://github.com/Fission-AI/OpenSpec) is the source of the compatible project document convention. No OpenSpec runtime, generated skill, or CLI implementation is bundled or required. External links in this package identify sources; they are not setup steps.

## pstack design references

The project-verification and method-evaluation guidance was independently written with reference to [Cursor pstack](https://github.com/cursor/plugins/tree/c5db7fef1f1b1ebb2d4b7ae0308bf4beb10cb4c1/pstack), revision `c5db7fef1f1b1ebb2d4b7ae0308bf4beb10cb4c1`, especially its `create-verification-skill`, `maintain-verification-skill`, and `poteto-mode/playbooks/eval.md` workflows. No pstack scripts, agent definitions, runtime dependencies or model configuration are bundled. Hippo Spec retains project-owned maps, scoped maintenance and explicit authorization rather than importing the upstream autonomous-operation defaults.

## Matt Pocock Skills license

MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
