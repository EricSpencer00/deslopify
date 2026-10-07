# Model catalog and repository files

<!-- CATALOG TREE START -->
## File tree

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug.yml — tooling bug and question form
│   │   ├── config.yml — issue chooser configuration
│   │   └── rule.yml — do/don't contribution form
│   └── workflows/
│       ├── pages.yml — build and deploy the website
│       ├── readme-tree.yml — CI update job
│       └── rule-proposal.yml — validate issues and propose add/change PRs
├── deslopify/
│   ├── examples/
│   │   └── website-copy.md — repository file
│   ├── fac/
│   │   └── _template/
│   │       ├── models/ — company model slots
│   │       │   ├── ai21/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── jamba-reasoning-3b.md
│   │       │   │   │   ├── jamba2-3b.md
│   │       │   │   │   └── jamba2-mini.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── jamba-1.6.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── alibaba/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── qwen3-coder-next.md
│   │       │   │   │   ├── qwen3-coder-plus.md
│   │       │   │   │   ├── qwen3-coder.md
│   │       │   │   │   ├── qwen3-max.md
│   │       │   │   │   ├── qwen3-next.md
│   │       │   │   │   ├── qwen3-vl-32b-thinking.md
│   │       │   │   │   ├── qwen3.5.md
│   │       │   │   │   ├── qwen3.6-plus.md
│   │       │   │   │   ├── qwen3.7-max.md
│   │       │   │   │   ├── qwen3.7-plus.md
│   │       │   │   │   ├── qwen3.8-omni-flash.md
│   │       │   │   │   └── qwen3.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── qwen2.5-coder.md
│   │       │   │   │   ├── qwen2.5.md
│   │       │   │   │   └── qwq-32b.md
│   │       │   │   ├── new/ — Qwen Code model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   └── qwen3.5-plus.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── allenai/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── olmo-3-instruct.md
│   │       │   │   │   ├── olmo-3-think.md
│   │       │   │   │   ├── olmo-3.1-instruct.md
│   │       │   │   │   └── olmo-3.1-think.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── olmo-2.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── amazon/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── nova-2-lite.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── nova-lite.md
│   │       │   │   │   ├── nova-micro.md
│   │       │   │   │   ├── nova-premier.md
│   │       │   │   │   └── nova-pro.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── anthropic/
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── claude-haiku-3.5.md
│   │       │   │   │   ├── claude-haiku-3.md
│   │       │   │   │   ├── claude-opus-3.md
│   │       │   │   │   ├── claude-opus-4.1.md
│   │       │   │   │   ├── claude-opus-4.md
│   │       │   │   │   ├── claude-sonnet-3.5.md
│   │       │   │   │   ├── claude-sonnet-3.7.md
│   │       │   │   │   ├── claude-sonnet-3.md
│   │       │   │   │   └── claude-sonnet-4.md
│   │       │   │   ├── new/ — Claude Code model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   ├── claude-fable-5.1.md
│   │       │   │   │   ├── claude-fable-5.md
│   │       │   │   │   ├── claude-haiku-4.5.md
│   │       │   │   │   ├── claude-opus-4.5.md
│   │       │   │   │   ├── claude-opus-4.6.md
│   │       │   │   │   ├── claude-opus-4.7.md
│   │       │   │   │   ├── claude-opus-4.8.md
│   │       │   │   │   ├── claude-opus-5.5.md
│   │       │   │   │   ├── claude-opus-5.md
│   │       │   │   │   ├── claude-sonnet-4.5.md
│   │       │   │   │   ├── claude-sonnet-4.6.md
│   │       │   │   │   ├── claude-sonnet-5.5.md
│   │       │   │   │   └── claude-sonnet-5.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── bytedance/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── seed-2.1-pro.md
│   │       │   │   │   └── seed-2.1-turbo.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── seed-2.0-code.md
│   │       │   │   │   ├── seed-2.0-lite.md
│   │       │   │   │   ├── seed-2.0-mini.md
│   │       │   │   │   └── seed-2.0-pro.md
│   │       │   │   ├── new/ — Trae model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   └── seed-code.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── cohere/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── command-a-plus.md
│   │       │   │   │   ├── command-a-reasoning.md
│   │       │   │   │   ├── command-a-translate.md
│   │       │   │   │   ├── command-a-vision.md
│   │       │   │   │   └── command-a.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── command-r-32b.md — model guidance
│   │       │   │   │   ├── command-r-plus.md
│   │       │   │   │   ├── command-r.md
│   │       │   │   │   └── command-r7b.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── deepseek/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── deepseek-v4-flash.md
│   │       │   │   │   ├── deepseek-v4-pro.md
│   │       │   │   │   └── deepseek-v4.1-flash.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── deepseek-coder-v2.md
│   │       │   │   │   ├── deepseek-r1-0528.md
│   │       │   │   │   ├── deepseek-r1.md
│   │       │   │   │   ├── deepseek-v3.1-terminus.md
│   │       │   │   │   ├── deepseek-v3.1.md
│   │       │   │   │   ├── deepseek-v3.2-speciale.md
│   │       │   │   │   ├── deepseek-v3.2.md
│   │       │   │   │   └── deepseek-v3.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── google/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── gemini-2.5-flash-lite.md
│   │       │   │   │   ├── gemini-2.5-flash.md
│   │       │   │   │   ├── gemini-2.5-pro.md
│   │       │   │   │   ├── gemini-3-pro.md
│   │       │   │   │   ├── gemini-3.1-flash-lite.md
│   │       │   │   │   ├── gemini-3.5-flash-lite.md
│   │       │   │   │   ├── gemini-3.5-flash.md
│   │       │   │   │   ├── gemini-3.6-flash.md
│   │       │   │   │   ├── gemini-3.7-flash.md
│   │       │   │   │   ├── gemini-3.8-flash.md
│   │       │   │   │   ├── gemma-2.md
│   │       │   │   │   ├── gemma-3.md
│   │       │   │   │   ├── gemma-3n.md
│   │       │   │   │   └── gemma-4.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── gemini-1.5-flash.md
│   │       │   │   │   ├── gemini-1.5-pro.md
│   │       │   │   │   ├── gemini-2.0-flash-lite.md
│   │       │   │   │   └── gemini-2.0-flash.md
│   │       │   │   ├── new/ — Gemini CLI/Jules model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   ├── gemini-3-flash.md
│   │       │   │   │   ├── gemini-3.1-pro.md
│   │       │   │   │   └── gemini-auto.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── ibm/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── granite-4.1.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── granite-4.0.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── meta/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── llama-4-maverick.md
│   │       │   │   │   └── llama-4-scout.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── llama-3.1.md
│   │       │   │   │   ├── llama-3.2-vision.md
│   │       │   │   │   ├── llama-3.2.md
│   │       │   │   │   ├── llama-3.3-70b.md
│   │       │   │   │   ├── llama-3.3.md
│   │       │   │   │   └── llama-3.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── microsoft/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── phi-4-mini-instruct.md
│   │       │   │   │   ├── phi-4-mini-reasoning.md
│   │       │   │   │   ├── phi-4-multimodal-instruct.md
│   │       │   │   │   ├── phi-4-reasoning.md
│   │       │   │   │   └── phi-4.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── minimax/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── minimax-m2.7.md
│   │       │   │   │   └── minimax-m3.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── minimax-m1.md
│   │       │   │   │   ├── minimax-m2.1.md
│   │       │   │   │   ├── minimax-m2.5.md
│   │       │   │   │   └── minimax-m2.md
│   │       │   │   ├── new/ — MiniMax Code model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   └── minimax-m3.1-flash-preview.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── mistral/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── codestral.md
│   │       │   │   │   ├── ministral-3-14b.md
│   │       │   │   │   ├── ministral-3-3b.md
│   │       │   │   │   ├── ministral-3-8b.md
│   │       │   │   │   ├── mistral-large-3.md
│   │       │   │   │   ├── mistral-medium-3.5.md
│   │       │   │   │   └── mistral-small-4.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── devstral-2.md
│   │       │   │   │   ├── devstral-small-2.md
│   │       │   │   │   ├── magistral-medium-1.2.md
│   │       │   │   │   ├── magistral-small-1.2.md
│   │       │   │   │   ├── mistral-large-2.1.md
│   │       │   │   │   ├── mistral-medium-3.1.md
│   │       │   │   │   ├── mistral-nemo.md — model guidance
│   │       │   │   │   ├── mistral-small-3.2.md
│   │       │   │   │   └── mistral-small-creative.md
│   │       │   │   ├── new/ — Mistral Vibe model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   └── mistral-medium-latest.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── moonshot/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── kimi-k2-thinking.md — model guidance
│   │       │   │   │   ├── kimi-k2.7-code.md
│   │       │   │   │   └── kimi-k2.8-preview.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── kimi-k2.5.md
│   │       │   │   │   ├── kimi-k2.6.md
│   │       │   │   │   └── kimi-k2.md
│   │       │   │   ├── new/ — Kimi Code model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   ├── kimi-for-coding-highspeed.md
│   │       │   │   │   ├── kimi-for-coding.md
│   │       │   │   │   └── kimi-k3.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── nvidia/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── nemotron-3-nano.md
│   │       │   │   │   ├── nemotron-3-super.md
│   │       │   │   │   └── nemotron-3-ultra.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   └── llama-3.1-nemotron-70b.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── openai/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── gpt-4.1-mini.md
│   │       │   │   │   ├── gpt-4.1-nano.md
│   │       │   │   │   ├── gpt-4.1.md
│   │       │   │   │   ├── gpt-4o-mini.md
│   │       │   │   │   ├── gpt-4o.md
│   │       │   │   │   ├── gpt-5-chat.md
│   │       │   │   │   ├── gpt-5-mini.md
│   │       │   │   │   ├── gpt-5-nano.md
│   │       │   │   │   ├── gpt-5-pro.md
│   │       │   │   │   ├── gpt-5.1.md
│   │       │   │   │   ├── gpt-5.2-pro.md
│   │       │   │   │   ├── gpt-5.2.md
│   │       │   │   │   ├── gpt-5.3-codex.md
│   │       │   │   │   ├── gpt-5.4-mini.md
│   │       │   │   │   ├── gpt-5.4-nano.md
│   │       │   │   │   ├── gpt-5.4-pro.md
│   │       │   │   │   ├── gpt-5.4.md
│   │       │   │   │   ├── gpt-5.5-pro.md
│   │       │   │   │   ├── gpt-5.md
│   │       │   │   │   ├── gpt-oss-120b.md
│   │       │   │   │   ├── gpt-oss-20b.md
│   │       │   │   │   ├── o1-mini.md
│   │       │   │   │   ├── o1-pro.md
│   │       │   │   │   ├── o1.md
│   │       │   │   │   ├── o3-mini.md
│   │       │   │   │   ├── o3-pro.md
│   │       │   │   │   ├── o3.md
│   │       │   │   │   └── o4-mini.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── codex-mini-latest.md
│   │       │   │   │   ├── gpt-3.5-turbo.md
│   │       │   │   │   ├── gpt-4-turbo.md
│   │       │   │   │   ├── gpt-4.5-preview.md
│   │       │   │   │   ├── gpt-5-codex-mini.md
│   │       │   │   │   ├── gpt-5-codex.md
│   │       │   │   │   ├── gpt-5.1-chat.md
│   │       │   │   │   ├── gpt-5.1-codex-max.md
│   │       │   │   │   ├── gpt-5.1-codex-mini.md
│   │       │   │   │   ├── gpt-5.1-codex.md
│   │       │   │   │   ├── gpt-5.2-chat.md
│   │       │   │   │   ├── gpt-5.2-codex.md
│   │       │   │   │   ├── gpt-5.3-chat.md
│   │       │   │   │   └── gpt-5.3-codex-spark.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   ├── gpt-5.5.md
│   │       │   │   │   ├── gpt-5.6-luna.md
│   │       │   │   │   ├── gpt-5.6-sol.md
│   │       │   │   │   ├── gpt-5.6-terra.md
│   │       │   │   │   ├── gpt-6-astra.md
│   │       │   │   │   ├── gpt-6-luna.md
│   │       │   │   │   ├── gpt-6-sol.md
│   │       │   │   │   └── gpt-6.1-sol.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── perplexity/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── sonar-deep-research.md
│   │       │   │   │   ├── sonar-pro.md
│   │       │   │   │   ├── sonar-reasoning-pro.md
│   │       │   │   │   ├── sonar-reasoning.md
│   │       │   │   │   └── sonar.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── writer/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── palmyra-x5.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── palmyra-x4.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── xai/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── grok-4.20.md
│   │       │   │   │   └── grok-4.3.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── grok-3-mini.md
│   │       │   │   │   ├── grok-3.md
│   │       │   │   │   ├── grok-4-fast.md
│   │       │   │   │   ├── grok-4.1-fast.md
│   │       │   │   │   ├── grok-4.md
│   │       │   │   │   └── grok-code-fast-1.md
│   │       │   │   ├── new/ — Grok Build model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   ├── grok-4.5.md
│   │       │   │   │   ├── grok-4.6.md
│   │       │   │   │   ├── grok-4.7-fast.md
│   │       │   │   │   ├── grok-4.7.md
│   │       │   │   │   └── grok-build-0.1.md
│   │       │   │   └── general.md — company guidance
│   │       │   └── z-ai/
│   │       │       ├── available/ — provider/API model slots
│   │       │       │   ├── glm-4.7-flash.md
│   │       │       │   └── glm-5.3-flashx.md
│   │       │       ├── deprecated/ — legacy model slots
│   │       │       │   ├── glm-4.5-air.md
│   │       │       │   ├── glm-4.5.md
│   │       │       │   ├── glm-4.6.md
│   │       │       │   ├── glm-4.7.md
│   │       │       │   ├── glm-5.1.md — model guidance
│   │       │       │   ├── glm-5.2.md
│   │       │       │   └── glm-5.md
│   │       │       ├── new/ — ZCode model slots
│   │       │       │   ├── .gitkeep — keeps an empty directory tracked
│   │       │       │   ├── glm-5.3-flash.md
│   │       │       │   └── glm-5.3.md
│   │       │       └── general.md — company guidance
│   │       └── general.md — all-model guidance
│   ├── ne-fac/
│   │   └── _template/
│   │       ├── models/ — company model slots
│   │       │   ├── ai21/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── jamba-reasoning-3b.md
│   │       │   │   │   ├── jamba2-3b.md
│   │       │   │   │   └── jamba2-mini.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── jamba-1.6.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── alibaba/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── qwen3-coder-next.md
│   │       │   │   │   ├── qwen3-coder-plus.md
│   │       │   │   │   ├── qwen3-coder.md
│   │       │   │   │   ├── qwen3-max.md
│   │       │   │   │   ├── qwen3-next.md
│   │       │   │   │   ├── qwen3-vl-32b-thinking.md — model guidance
│   │       │   │   │   ├── qwen3.5.md
│   │       │   │   │   ├── qwen3.6-plus.md
│   │       │   │   │   ├── qwen3.7-max.md
│   │       │   │   │   ├── qwen3.7-plus.md
│   │       │   │   │   ├── qwen3.8-omni-flash.md
│   │       │   │   │   └── qwen3.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── qwen2.5-coder.md
│   │       │   │   │   ├── qwen2.5.md
│   │       │   │   │   └── qwq-32b.md
│   │       │   │   ├── new/ — Qwen Code model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   └── qwen3.5-plus.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── allenai/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── olmo-3-instruct.md
│   │       │   │   │   ├── olmo-3-think.md
│   │       │   │   │   ├── olmo-3.1-instruct.md
│   │       │   │   │   └── olmo-3.1-think.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── olmo-2.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── amazon/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── nova-2-lite.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── nova-lite.md
│   │       │   │   │   ├── nova-micro.md
│   │       │   │   │   ├── nova-premier.md
│   │       │   │   │   └── nova-pro.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── anthropic/
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── claude-haiku-3.5.md
│   │       │   │   │   ├── claude-haiku-3.md
│   │       │   │   │   ├── claude-opus-3.md
│   │       │   │   │   ├── claude-opus-4.1.md
│   │       │   │   │   ├── claude-opus-4.md
│   │       │   │   │   ├── claude-sonnet-3.5.md
│   │       │   │   │   ├── claude-sonnet-3.7.md
│   │       │   │   │   ├── claude-sonnet-3.md
│   │       │   │   │   └── claude-sonnet-4.md
│   │       │   │   ├── new/ — Claude Code model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   ├── claude-fable-5.1.md
│   │       │   │   │   ├── claude-fable-5.md
│   │       │   │   │   ├── claude-haiku-4.5.md
│   │       │   │   │   ├── claude-opus-4.5.md
│   │       │   │   │   ├── claude-opus-4.6.md
│   │       │   │   │   ├── claude-opus-4.7.md
│   │       │   │   │   ├── claude-opus-4.8.md
│   │       │   │   │   ├── claude-opus-5.5.md
│   │       │   │   │   ├── claude-opus-5.md
│   │       │   │   │   ├── claude-sonnet-4.5.md
│   │       │   │   │   ├── claude-sonnet-4.6.md
│   │       │   │   │   ├── claude-sonnet-5.5.md
│   │       │   │   │   └── claude-sonnet-5.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── bytedance/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── seed-2.1-pro.md
│   │       │   │   │   └── seed-2.1-turbo.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── seed-2.0-code.md
│   │       │   │   │   ├── seed-2.0-lite.md
│   │       │   │   │   ├── seed-2.0-mini.md
│   │       │   │   │   └── seed-2.0-pro.md
│   │       │   │   ├── new/ — Trae model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   └── seed-code.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── cohere/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── command-a-plus.md
│   │       │   │   │   ├── command-a-reasoning.md
│   │       │   │   │   ├── command-a-translate.md
│   │       │   │   │   ├── command-a-vision.md
│   │       │   │   │   └── command-a.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── command-r-32b.md
│   │       │   │   │   ├── command-r-plus.md
│   │       │   │   │   ├── command-r.md
│   │       │   │   │   └── command-r7b.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── deepseek/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── deepseek-v4-flash.md
│   │       │   │   │   ├── deepseek-v4-pro.md
│   │       │   │   │   └── deepseek-v4.1-flash.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── deepseek-coder-v2.md
│   │       │   │   │   ├── deepseek-r1-0528.md
│   │       │   │   │   ├── deepseek-r1.md
│   │       │   │   │   ├── deepseek-v3.1-terminus.md
│   │       │   │   │   ├── deepseek-v3.1.md
│   │       │   │   │   ├── deepseek-v3.2-speciale.md
│   │       │   │   │   ├── deepseek-v3.2.md
│   │       │   │   │   └── deepseek-v3.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── google/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── gemini-2.5-flash-lite.md
│   │       │   │   │   ├── gemini-2.5-flash.md
│   │       │   │   │   ├── gemini-2.5-pro.md — model guidance
│   │       │   │   │   ├── gemini-3-pro.md
│   │       │   │   │   ├── gemini-3.1-flash-lite.md
│   │       │   │   │   ├── gemini-3.5-flash-lite.md
│   │       │   │   │   ├── gemini-3.5-flash.md
│   │       │   │   │   ├── gemini-3.6-flash.md
│   │       │   │   │   ├── gemini-3.7-flash.md
│   │       │   │   │   ├── gemini-3.8-flash.md
│   │       │   │   │   ├── gemma-2.md
│   │       │   │   │   ├── gemma-3.md
│   │       │   │   │   ├── gemma-3n.md
│   │       │   │   │   └── gemma-4.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── gemini-1.5-flash.md
│   │       │   │   │   ├── gemini-1.5-pro.md
│   │       │   │   │   ├── gemini-2.0-flash-lite.md
│   │       │   │   │   └── gemini-2.0-flash.md
│   │       │   │   ├── new/ — Gemini CLI/Jules model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   ├── gemini-3-flash.md
│   │       │   │   │   ├── gemini-3.1-pro.md
│   │       │   │   │   └── gemini-auto.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── ibm/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── granite-4.1.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── granite-4.0.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── meta/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── llama-4-maverick.md
│   │       │   │   │   └── llama-4-scout.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── llama-3.1.md
│   │       │   │   │   ├── llama-3.2-vision.md
│   │       │   │   │   ├── llama-3.2.md
│   │       │   │   │   ├── llama-3.3-70b.md — model guidance
│   │       │   │   │   ├── llama-3.3.md
│   │       │   │   │   └── llama-3.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── microsoft/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── phi-4-mini-instruct.md
│   │       │   │   │   ├── phi-4-mini-reasoning.md
│   │       │   │   │   ├── phi-4-multimodal-instruct.md
│   │       │   │   │   ├── phi-4-reasoning.md
│   │       │   │   │   └── phi-4.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── minimax/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── minimax-m2.7.md
│   │       │   │   │   └── minimax-m3.md — model guidance
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── minimax-m1.md
│   │       │   │   │   ├── minimax-m2.1.md
│   │       │   │   │   ├── minimax-m2.5.md
│   │       │   │   │   └── minimax-m2.md
│   │       │   │   ├── new/ — MiniMax Code model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   └── minimax-m3.1-flash-preview.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── mistral/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── codestral.md
│   │       │   │   │   ├── ministral-3-14b.md
│   │       │   │   │   ├── ministral-3-3b.md
│   │       │   │   │   ├── ministral-3-8b.md
│   │       │   │   │   ├── mistral-large-3.md
│   │       │   │   │   ├── mistral-medium-3.5.md
│   │       │   │   │   └── mistral-small-4.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── devstral-2.md
│   │       │   │   │   ├── devstral-small-2.md
│   │       │   │   │   ├── magistral-medium-1.2.md
│   │       │   │   │   ├── magistral-small-1.2.md
│   │       │   │   │   ├── mistral-large-2.1.md
│   │       │   │   │   ├── mistral-medium-3.1.md
│   │       │   │   │   ├── mistral-nemo.md
│   │       │   │   │   ├── mistral-small-3.2.md
│   │       │   │   │   └── mistral-small-creative.md
│   │       │   │   ├── new/ — Mistral Vibe model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   └── mistral-medium-latest.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── moonshot/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── kimi-k2-thinking.md
│   │       │   │   │   ├── kimi-k2.7-code.md
│   │       │   │   │   └── kimi-k2.8-preview.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── kimi-k2.5.md
│   │       │   │   │   ├── kimi-k2.6.md
│   │       │   │   │   └── kimi-k2.md
│   │       │   │   ├── new/ — Kimi Code model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   ├── kimi-for-coding-highspeed.md
│   │       │   │   │   ├── kimi-for-coding.md
│   │       │   │   │   └── kimi-k3.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── nvidia/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── nemotron-3-nano.md
│   │       │   │   │   ├── nemotron-3-super.md
│   │       │   │   │   └── nemotron-3-ultra.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   └── llama-3.1-nemotron-70b.md — model guidance
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── openai/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── gpt-4.1-mini.md
│   │       │   │   │   ├── gpt-4.1-nano.md
│   │       │   │   │   ├── gpt-4.1.md
│   │       │   │   │   ├── gpt-4o-mini.md
│   │       │   │   │   ├── gpt-4o.md
│   │       │   │   │   ├── gpt-5-chat.md
│   │       │   │   │   ├── gpt-5-mini.md
│   │       │   │   │   ├── gpt-5-nano.md
│   │       │   │   │   ├── gpt-5-pro.md
│   │       │   │   │   ├── gpt-5.1.md
│   │       │   │   │   ├── gpt-5.2-pro.md
│   │       │   │   │   ├── gpt-5.2.md
│   │       │   │   │   ├── gpt-5.3-codex.md
│   │       │   │   │   ├── gpt-5.4-mini.md
│   │       │   │   │   ├── gpt-5.4-nano.md
│   │       │   │   │   ├── gpt-5.4-pro.md
│   │       │   │   │   ├── gpt-5.4.md — model guidance
│   │       │   │   │   ├── gpt-5.5-pro.md
│   │       │   │   │   ├── gpt-5.md
│   │       │   │   │   ├── gpt-oss-120b.md
│   │       │   │   │   ├── gpt-oss-20b.md
│   │       │   │   │   ├── o1-mini.md
│   │       │   │   │   ├── o1-pro.md
│   │       │   │   │   ├── o1.md
│   │       │   │   │   ├── o3-mini.md
│   │       │   │   │   ├── o3-pro.md
│   │       │   │   │   ├── o3.md
│   │       │   │   │   └── o4-mini.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── codex-mini-latest.md
│   │       │   │   │   ├── gpt-3.5-turbo.md
│   │       │   │   │   ├── gpt-4-turbo.md
│   │       │   │   │   ├── gpt-4.5-preview.md
│   │       │   │   │   ├── gpt-5-codex-mini.md
│   │       │   │   │   ├── gpt-5-codex.md
│   │       │   │   │   ├── gpt-5.1-chat.md
│   │       │   │   │   ├── gpt-5.1-codex-max.md
│   │       │   │   │   ├── gpt-5.1-codex-mini.md
│   │       │   │   │   ├── gpt-5.1-codex.md
│   │       │   │   │   ├── gpt-5.2-chat.md
│   │       │   │   │   ├── gpt-5.2-codex.md
│   │       │   │   │   ├── gpt-5.3-chat.md
│   │       │   │   │   └── gpt-5.3-codex-spark.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   ├── gpt-5.5.md — model guidance
│   │       │   │   │   ├── gpt-5.6-luna.md
│   │       │   │   │   ├── gpt-5.6-sol.md
│   │       │   │   │   ├── gpt-5.6-terra.md
│   │       │   │   │   ├── gpt-6-astra.md
│   │       │   │   │   ├── gpt-6-luna.md
│   │       │   │   │   ├── gpt-6-sol.md
│   │       │   │   │   └── gpt-6.1-sol.md
│   │       │   │   └── general.md — company guidance
│   │       │   ├── perplexity/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── sonar-deep-research.md
│   │       │   │   │   ├── sonar-pro.md
│   │       │   │   │   ├── sonar-reasoning-pro.md
│   │       │   │   │   ├── sonar-reasoning.md
│   │       │   │   │   └── sonar.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── writer/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── palmyra-x5.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── palmyra-x4.md
│   │       │   │   ├── new/ — provider-native model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — company guidance
│   │       │   ├── xai/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── grok-4.20.md
│   │       │   │   │   └── grok-4.3.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── grok-3-mini.md
│   │       │   │   │   ├── grok-3.md
│   │       │   │   │   ├── grok-4-fast.md
│   │       │   │   │   ├── grok-4.1-fast.md
│   │       │   │   │   ├── grok-4.md
│   │       │   │   │   └── grok-code-fast-1.md
│   │       │   │   ├── new/ — Grok Build model slots
│   │       │   │   │   ├── .gitkeep — keeps an empty directory tracked
│   │       │   │   │   ├── grok-4.5.md
│   │       │   │   │   ├── grok-4.6.md
│   │       │   │   │   ├── grok-4.7-fast.md
│   │       │   │   │   ├── grok-4.7.md
│   │       │   │   │   └── grok-build-0.1.md
│   │       │   │   └── general.md — company guidance
│   │       │   └── z-ai/
│   │       │       ├── available/ — provider/API model slots
│   │       │       │   ├── glm-4.7-flash.md
│   │       │       │   └── glm-5.3-flashx.md
│   │       │       ├── deprecated/ — legacy model slots
│   │       │       │   ├── glm-4.5-air.md
│   │       │       │   ├── glm-4.5.md
│   │       │       │   ├── glm-4.6.md
│   │       │       │   ├── glm-4.7.md
│   │       │       │   ├── glm-5.1.md
│   │       │       │   ├── glm-5.2.md
│   │       │       │   └── glm-5.md
│   │       │       ├── new/ — ZCode model slots
│   │       │       │   ├── .gitkeep — keeps an empty directory tracked
│   │       │       │   ├── glm-5.3-flash.md
│   │       │       │   └── glm-5.3.md
│   │       │       └── general.md — company guidance
│   │       └── general.md — all-model guidance
│   ├── references/
│   │   ├── rule-index.json — machine-readable rule index
│   │   └── rule-index.md — browsable rule index
│   ├── rules/ — canonical writing, taste, and design records
│   │   ├── design/
│   │   │   ├── preserve-needed-ui-copy.json — canonical rule record
│   │   │   └── remove-redundant-ui-copy.json — canonical rule record
│   │   ├── taste/
│   │   │   └── meaning-before-phrase-lists.json — canonical rule record
│   │   └── writing/
│   │       ├── about-pages-answer-questions.json — canonical rule record
│   │       ├── alibaba-dont-repeat-taglines.json — canonical rule record
│   │       ├── anthropic-concrete-fiction-details.json — canonical rule record
│   │       ├── anthropic-dont-invent-experiences.json — canonical rule record
│   │       ├── anthropic-plain-technical-language.json — canonical rule record
│   │       ├── argument-led-length.json — canonical rule record
│   │       ├── audience-relevant-details.json — canonical rule record
│   │       ├── cohere-retain-character-details.json — canonical rule record
│   │       ├── cut-repetition.json — canonical rule record
│   │       ├── deepseek-edit-without-inflation.json — canonical rule record
│   │       ├── dont-diagnose-authorship-by-polish.json — canonical rule record
│   │       ├── dont-fake-human-errors.json — canonical rule record
│   │       ├── dont-repeat-aphorisms.json — canonical rule record
│   │       ├── google-dont-add-stock-fiction.json — canonical rule record
│   │       ├── meta-preserve-scene-detail.json — canonical rule record
│   │       ├── minimax-preserve-distinct-passages.json — canonical rule record
│   │       ├── mistral-distinct-alternatives.json — canonical rule record
│   │       ├── moonshot-check-continuity.json — canonical rule record
│   │       ├── nvidia-continuous-prose.json — canonical rule record
│   │       ├── omit-unneeded-version-history.json — canonical rule record
│   │       ├── openai-no-academic-boilerplate.json — canonical rule record
│   │       ├── openai-no-unfitting-creatures.json — canonical rule record
│   │       ├── openai-no-unrelated-creatures.json — canonical rule record
│   │       ├── preserve-author-voice.json — canonical rule record
│   │       ├── public-copy-without-diagnostics.json — canonical rule record
│   │       ├── support-vague-claims.json — canonical rule record
│   │       ├── useful-product-specs.json — canonical rule record
│   │       ├── xai-new-ideas.json — canonical rule record
│   │       ├── xai-vary-repeated-actions.json — canonical rule record
│   │       └── z-ai-preserve-dialogue-conventions.json — canonical rule record
│   ├── scripts/
│   │   └── rules.py — validate, generate, and select rules
│   └── SKILL.md — skill entrypoint
├── scripts/
│   ├── build_site.py — website generator
│   ├── propose_rule.py — issue-form parser and add/change helper
│   ├── rule_pull_request.py — issue-to-PR Actions entrypoint
│   ├── sync_model_harnesses.py — provider-native model slot sync
│   ├── update_readme_tree.py — catalog generator
│   └── validate_content.py — repository file
├── site/
│   ├── app.js — rule filters and copy buttons
│   ├── favicon.svg — website icon
│   ├── index.html — website page template
│   ├── og.png — link preview image
│   └── style.css — website styles
├── tests/
│   ├── fixtures/
│   │   └── rewrites.json — repository file
│   ├── test_content.py — repository file
│   ├── test_rule_pull_request.py — repository file
│   ├── test_rules.py — repository file
│   └── test_site.py — website build tests
├── .gitignore — repository file
├── AGENTS.md — agent maintenance guide
├── CONTRIBUTING.md — rule form, example pair, and Actions workflow
├── LICENSE — license
├── MODEL-CATALOG.md — model catalog and repository map
└── README.md — purpose, installation, and usage
```

### File notes

- `_template/general.md` applies to all models; company `general.md` files apply to that company.
- Populated model files name the model, any harness or setting, and the writing context. Empty files are unused slots.
- `.gitkeep` files keep empty model-state directories in Git.
<!-- CATALOG TREE END -->
