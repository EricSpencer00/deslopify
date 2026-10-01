# deslopify
remove AI-generated -isms from your emails, website designs, or "[slop-grenades](https://noslopgrenade.com/)"

<!-- README TREE START -->
## File tree

```text
.
├── .github/
│   └── workflows/
│       └── readme-tree.yml — CI update job
├── deslopify/
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
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── alibaba/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── qwen3-coder-next.md
│   │       │   │   │   ├── qwen3-coder-plus.md
│   │       │   │   │   ├── qwen3-coder.md
│   │       │   │   │   ├── qwen3-max.md
│   │       │   │   │   ├── qwen3-next.md
│   │       │   │   │   ├── qwen3.5-plus.md
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
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── allenai/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── olmo-3-instruct.md
│   │       │   │   │   ├── olmo-3-think.md
│   │       │   │   │   ├── olmo-3.1-instruct.md
│   │       │   │   │   └── olmo-3.1-think.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── olmo-2.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── amazon/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── nova-2-lite.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── nova-lite.md
│   │       │   │   │   ├── nova-micro.md
│   │       │   │   │   ├── nova-premier.md
│   │       │   │   │   └── nova-pro.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── anthropic/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── claude-fable-5.1.md
│   │       │   │   │   ├── claude-opus-3.md
│   │       │   │   │   ├── claude-opus-5.5.md
│   │       │   │   │   └── claude-sonnet-5.5.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── claude-fable-5.md
│   │       │   │   │   ├── claude-haiku-3.5.md
│   │       │   │   │   ├── claude-haiku-3.md
│   │       │   │   │   ├── claude-haiku-4.5.md
│   │       │   │   │   ├── claude-opus-4.1.md
│   │       │   │   │   ├── claude-opus-4.5.md
│   │       │   │   │   ├── claude-opus-4.6.md
│   │       │   │   │   ├── claude-opus-4.7.md
│   │       │   │   │   ├── claude-opus-4.8.md
│   │       │   │   │   ├── claude-opus-4.md
│   │       │   │   │   ├── claude-opus-5.md
│   │       │   │   │   ├── claude-sonnet-3.5.md
│   │       │   │   │   ├── claude-sonnet-3.7.md
│   │       │   │   │   ├── claude-sonnet-3.md
│   │       │   │   │   ├── claude-sonnet-4.5.md
│   │       │   │   │   ├── claude-sonnet-4.6.md
│   │       │   │   │   ├── claude-sonnet-4.md
│   │       │   │   │   └── claude-sonnet-5.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── bytedance/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── seed-2.1-pro.md
│   │       │   │   │   └── seed-2.1-turbo.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── seed-2.0-code.md
│   │       │   │   │   ├── seed-2.0-lite.md
│   │       │   │   │   ├── seed-2.0-mini.md
│   │       │   │   │   └── seed-2.0-pro.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── cohere/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── command-a-plus.md
│   │       │   │   │   ├── command-a-reasoning.md
│   │       │   │   │   ├── command-a-translate.md
│   │       │   │   │   ├── command-a-vision.md
│   │       │   │   │   └── command-a.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── command-r-plus.md
│   │       │   │   │   ├── command-r.md
│   │       │   │   │   └── command-r7b.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
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
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── google/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── gemini-2.5-flash-lite.md
│   │       │   │   │   ├── gemini-2.5-flash.md
│   │       │   │   │   ├── gemini-2.5-pro.md
│   │       │   │   │   ├── gemini-3-flash.md
│   │       │   │   │   ├── gemini-3-pro.md
│   │       │   │   │   ├── gemini-3.1-flash-lite.md
│   │       │   │   │   ├── gemini-3.1-pro.md
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
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── ibm/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── granite-4.1.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── granite-4.0.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── meta/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── llama-4-maverick.md
│   │       │   │   │   └── llama-4-scout.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── llama-3.1.md
│   │       │   │   │   ├── llama-3.2-vision.md
│   │       │   │   │   ├── llama-3.2.md
│   │       │   │   │   ├── llama-3.3.md
│   │       │   │   │   └── llama-3.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── microsoft/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── phi-4-mini-instruct.md
│   │       │   │   │   ├── phi-4-mini-reasoning.md
│   │       │   │   │   ├── phi-4-multimodal-instruct.md
│   │       │   │   │   ├── phi-4-reasoning.md
│   │       │   │   │   └── phi-4.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── minimax/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── minimax-m2.7.md
│   │       │   │   │   └── minimax-m3.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── minimax-m1.md
│   │       │   │   │   ├── minimax-m2.1.md
│   │       │   │   │   ├── minimax-m2.5.md
│   │       │   │   │   └── minimax-m2.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
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
│   │       │   │   │   ├── mistral-small-3.2.md
│   │       │   │   │   └── mistral-small-creative.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── moonshot/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── kimi-k2-thinking.md
│   │       │   │   │   ├── kimi-k2.7-code.md
│   │       │   │   │   ├── kimi-k2.8-preview.md
│   │       │   │   │   └── kimi-k3.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── kimi-k2.5.md
│   │       │   │   │   ├── kimi-k2.6.md
│   │       │   │   │   └── kimi-k2.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── nvidia/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── nemotron-3-nano.md
│   │       │   │   │   ├── nemotron-3-super.md
│   │       │   │   │   └── nemotron-3-ultra.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
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
│   │       │   │   │   ├── gpt-5.5.md
│   │       │   │   │   ├── gpt-5.6-luna.md
│   │       │   │   │   ├── gpt-5.6-terra.md
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
│   │       │   │   │   ├── gpt-3.5-turbo.md
│   │       │   │   │   ├── gpt-4-turbo.md
│   │       │   │   │   ├── gpt-4.5-preview.md
│   │       │   │   │   ├── gpt-5-codex.md
│   │       │   │   │   ├── gpt-5.1-chat.md
│   │       │   │   │   ├── gpt-5.1-codex-max.md
│   │       │   │   │   ├── gpt-5.1-codex-mini.md
│   │       │   │   │   ├── gpt-5.1-codex.md
│   │       │   │   │   ├── gpt-5.2-chat.md
│   │       │   │   │   ├── gpt-5.2-codex.md
│   │       │   │   │   └── gpt-5.3-chat.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   ├── gpt-5.6-sol.md
│   │       │   │   │   ├── gpt-6-astra.md
│   │       │   │   │   ├── gpt-6-luna.md
│   │       │   │   │   ├── gpt-6-sol.md
│   │       │   │   │   └── gpt-6.1-sol.md
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── perplexity/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── sonar-deep-research.md
│   │       │   │   │   ├── sonar-pro.md
│   │       │   │   │   ├── sonar-reasoning-pro.md
│   │       │   │   │   ├── sonar-reasoning.md
│   │       │   │   │   └── sonar.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── writer/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── palmyra-x5.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── palmyra-x4.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── xai/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── grok-4.20.md
│   │       │   │   │   ├── grok-4.3.md
│   │       │   │   │   ├── grok-4.6.md
│   │       │   │   │   ├── grok-4.7.md
│   │       │   │   │   └── grok-build-0.1.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── grok-3-mini.md
│   │       │   │   │   ├── grok-3.md
│   │       │   │   │   ├── grok-4-fast.md
│   │       │   │   │   ├── grok-4.1-fast.md
│   │       │   │   │   ├── grok-4.md
│   │       │   │   │   └── grok-code-fast-1.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   └── z-ai/
│   │       │       ├── available/ — provider/API model slots
│   │       │       │   ├── glm-4.7-flash.md
│   │       │       │   ├── glm-5.3-flash.md
│   │       │       │   ├── glm-5.3-flashx.md
│   │       │       │   └── glm-5.3.md
│   │       │       ├── deprecated/ — legacy model slots
│   │       │       │   ├── glm-4.5-air.md
│   │       │       │   ├── glm-4.5.md
│   │       │       │   ├── glm-4.6.md
│   │       │       │   ├── glm-4.7.md
│   │       │       │   ├── glm-5.1.md
│   │       │       │   ├── glm-5.2.md
│   │       │       │   └── glm-5.md
│   │       │       ├── new/ — Codex model slots
│   │       │       │   └── .gitkeep — keeps an empty directory tracked
│   │       │       └── general.md — general guidance slot
│   │       └── general.md — general guidance slot
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
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── alibaba/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── qwen3-coder-next.md
│   │       │   │   │   ├── qwen3-coder-plus.md
│   │       │   │   │   ├── qwen3-coder.md
│   │       │   │   │   ├── qwen3-max.md
│   │       │   │   │   ├── qwen3-next.md
│   │       │   │   │   ├── qwen3.5-plus.md
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
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── allenai/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── olmo-3-instruct.md
│   │       │   │   │   ├── olmo-3-think.md
│   │       │   │   │   ├── olmo-3.1-instruct.md
│   │       │   │   │   └── olmo-3.1-think.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── olmo-2.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── amazon/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── nova-2-lite.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── nova-lite.md
│   │       │   │   │   ├── nova-micro.md
│   │       │   │   │   ├── nova-premier.md
│   │       │   │   │   └── nova-pro.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── anthropic/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── claude-fable-5.1.md
│   │       │   │   │   ├── claude-opus-3.md
│   │       │   │   │   ├── claude-opus-5.5.md
│   │       │   │   │   └── claude-sonnet-5.5.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── claude-fable-5.md
│   │       │   │   │   ├── claude-haiku-3.5.md
│   │       │   │   │   ├── claude-haiku-3.md
│   │       │   │   │   ├── claude-haiku-4.5.md
│   │       │   │   │   ├── claude-opus-4.1.md
│   │       │   │   │   ├── claude-opus-4.5.md
│   │       │   │   │   ├── claude-opus-4.6.md
│   │       │   │   │   ├── claude-opus-4.7.md
│   │       │   │   │   ├── claude-opus-4.8.md
│   │       │   │   │   ├── claude-opus-4.md
│   │       │   │   │   ├── claude-opus-5.md
│   │       │   │   │   ├── claude-sonnet-3.5.md
│   │       │   │   │   ├── claude-sonnet-3.7.md
│   │       │   │   │   ├── claude-sonnet-3.md
│   │       │   │   │   ├── claude-sonnet-4.5.md
│   │       │   │   │   ├── claude-sonnet-4.6.md
│   │       │   │   │   ├── claude-sonnet-4.md
│   │       │   │   │   └── claude-sonnet-5.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── bytedance/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── seed-2.1-pro.md
│   │       │   │   │   └── seed-2.1-turbo.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── seed-2.0-code.md
│   │       │   │   │   ├── seed-2.0-lite.md
│   │       │   │   │   ├── seed-2.0-mini.md
│   │       │   │   │   └── seed-2.0-pro.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── cohere/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── command-a-plus.md
│   │       │   │   │   ├── command-a-reasoning.md
│   │       │   │   │   ├── command-a-translate.md
│   │       │   │   │   ├── command-a-vision.md
│   │       │   │   │   └── command-a.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── command-r-plus.md
│   │       │   │   │   ├── command-r.md
│   │       │   │   │   └── command-r7b.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
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
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── google/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── gemini-2.5-flash-lite.md
│   │       │   │   │   ├── gemini-2.5-flash.md
│   │       │   │   │   ├── gemini-2.5-pro.md
│   │       │   │   │   ├── gemini-3-flash.md
│   │       │   │   │   ├── gemini-3-pro.md
│   │       │   │   │   ├── gemini-3.1-flash-lite.md
│   │       │   │   │   ├── gemini-3.1-pro.md
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
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── ibm/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── granite-4.1.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── granite-4.0.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── meta/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── llama-4-maverick.md
│   │       │   │   │   └── llama-4-scout.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── llama-3.1.md
│   │       │   │   │   ├── llama-3.2-vision.md
│   │       │   │   │   ├── llama-3.2.md
│   │       │   │   │   ├── llama-3.3.md
│   │       │   │   │   └── llama-3.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── microsoft/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── phi-4-mini-instruct.md
│   │       │   │   │   ├── phi-4-mini-reasoning.md
│   │       │   │   │   ├── phi-4-multimodal-instruct.md
│   │       │   │   │   ├── phi-4-reasoning.md
│   │       │   │   │   └── phi-4.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── minimax/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── minimax-m2.7.md
│   │       │   │   │   └── minimax-m3.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── minimax-m1.md
│   │       │   │   │   ├── minimax-m2.1.md
│   │       │   │   │   ├── minimax-m2.5.md
│   │       │   │   │   └── minimax-m2.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
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
│   │       │   │   │   ├── mistral-small-3.2.md
│   │       │   │   │   └── mistral-small-creative.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── moonshot/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── kimi-k2-thinking.md
│   │       │   │   │   ├── kimi-k2.7-code.md
│   │       │   │   │   ├── kimi-k2.8-preview.md
│   │       │   │   │   └── kimi-k3.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── kimi-k2.5.md
│   │       │   │   │   ├── kimi-k2.6.md
│   │       │   │   │   └── kimi-k2.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── nvidia/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── nemotron-3-nano.md
│   │       │   │   │   ├── nemotron-3-super.md
│   │       │   │   │   └── nemotron-3-ultra.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
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
│   │       │   │   │   ├── gpt-5.5.md
│   │       │   │   │   ├── gpt-5.6-luna.md
│   │       │   │   │   ├── gpt-5.6-terra.md
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
│   │       │   │   │   ├── gpt-3.5-turbo.md
│   │       │   │   │   ├── gpt-4-turbo.md
│   │       │   │   │   ├── gpt-4.5-preview.md
│   │       │   │   │   ├── gpt-5-codex.md
│   │       │   │   │   ├── gpt-5.1-chat.md
│   │       │   │   │   ├── gpt-5.1-codex-max.md
│   │       │   │   │   ├── gpt-5.1-codex-mini.md
│   │       │   │   │   ├── gpt-5.1-codex.md
│   │       │   │   │   ├── gpt-5.2-chat.md
│   │       │   │   │   ├── gpt-5.2-codex.md
│   │       │   │   │   └── gpt-5.3-chat.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   ├── gpt-5.6-sol.md
│   │       │   │   │   ├── gpt-6-astra.md
│   │       │   │   │   ├── gpt-6-luna.md
│   │       │   │   │   ├── gpt-6-sol.md
│   │       │   │   │   └── gpt-6.1-sol.md
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── perplexity/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── sonar-deep-research.md
│   │       │   │   │   ├── sonar-pro.md
│   │       │   │   │   ├── sonar-reasoning-pro.md
│   │       │   │   │   ├── sonar-reasoning.md
│   │       │   │   │   └── sonar.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── writer/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   └── palmyra-x5.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   └── palmyra-x4.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   ├── xai/
│   │       │   │   ├── available/ — provider/API model slots
│   │       │   │   │   ├── grok-4.20.md
│   │       │   │   │   ├── grok-4.3.md
│   │       │   │   │   ├── grok-4.6.md
│   │       │   │   │   ├── grok-4.7.md
│   │       │   │   │   └── grok-build-0.1.md
│   │       │   │   ├── deprecated/ — legacy model slots
│   │       │   │   │   ├── grok-3-mini.md
│   │       │   │   │   ├── grok-3.md
│   │       │   │   │   ├── grok-4-fast.md
│   │       │   │   │   ├── grok-4.1-fast.md
│   │       │   │   │   ├── grok-4.md
│   │       │   │   │   └── grok-code-fast-1.md
│   │       │   │   ├── new/ — Codex model slots
│   │       │   │   │   └── .gitkeep — keeps an empty directory tracked
│   │       │   │   └── general.md — general guidance slot
│   │       │   └── z-ai/
│   │       │       ├── available/ — provider/API model slots
│   │       │       │   ├── glm-4.7-flash.md
│   │       │       │   ├── glm-5.3-flash.md
│   │       │       │   ├── glm-5.3-flashx.md
│   │       │       │   └── glm-5.3.md
│   │       │       ├── deprecated/ — legacy model slots
│   │       │       │   ├── glm-4.5-air.md
│   │       │       │   ├── glm-4.5.md
│   │       │       │   ├── glm-4.6.md
│   │       │       │   ├── glm-4.7.md
│   │       │       │   ├── glm-5.1.md
│   │       │       │   ├── glm-5.2.md
│   │       │       │   └── glm-5.md
│   │       │       ├── new/ — Codex model slots
│   │       │       │   └── .gitkeep — keeps an empty directory tracked
│   │       │       └── general.md — general guidance slot
│   │       └── general.md — general guidance slot
│   └── SKILL.md — skill entrypoint
├── scripts/
│   └── update_readme_tree.py — README tree generator
├── LICENSE — license
└── README.md — repository map
```

### File notes

- `general.md` is the company guidance slot.
- Model `.md` files are empty slots for model-specific guidance.
- `.gitkeep` files keep empty model-state directories in Git.
<!-- README TREE END -->