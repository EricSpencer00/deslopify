# deslopify
remove AI-generated -isms from your emails, website designs, or "[slop-grenades](https://noslopgrenade.com/)"

Start with [the skill](deslopify/SKILL.md) or [the website-copy examples](deslopify/examples/website-copy.md).

## Add a do or don't

[Fill out the rule form](https://github.com/EricSpencer00/deslopify/issues/new?template=rule.yml) with one example and one counterexample. Choose **writing**, **taste**, or **design**, and whether it applies to **all models**, **one company**, or **one model**. You can also use it to change an existing rule.

[Browse the rules](deslopify/references/rule-index.md) or read [how contributions become skill updates](CONTRIBUTING.md).

## Install and use

Copy the complete `deslopify/` folder into your project's `.agents/skills/deslopify/` directory. Keep its subfolders so linked guidance resolves.

Then include your draft and intended audience in a request such as:

```text
$deslopify Edit this draft for its audience while preserving meaning, useful facts, and needed qualifications.
```

<details>
<summary>Model catalog</summary>

[Browse all model slots and repository files](MODEL-CATALOG.md).

</details>

<details>
<summary>Related projects</summary>

Similar projects:
* [peteromallet/desloppify](https://github.com/peteromallet/desloppify) which focused on codebase management, not writing

And expands on the ideas of previous projects like:
* [shreyas-makes/deslopify](https://github.com/shreyas-makes/deslopify) 

</details>
