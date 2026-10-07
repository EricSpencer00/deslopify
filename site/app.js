// Progressive enhancement only: every rule is in the HTML without this file.
(() => {
  // Copy buttons on code blocks.
  for (const block of document.querySelectorAll(".code")) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "copy";
    button.textContent = "Copy";
    button.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(block.querySelector("code").innerText);
        button.textContent = "Copied";
      } catch {
        button.textContent = "Select and copy";
      }
      setTimeout(() => (button.textContent = "Copy"), 1600);
    });
    block.append(button);
  }

  // Rule filters.
  const form = document.querySelector(".filters");
  if (!form) return;
  const rules = [...document.querySelectorAll(".rule")];
  const groups = [...document.querySelectorAll(".rule-group")];
  const result = form.querySelector(".result");
  const empty = document.querySelector(".empty");
  form.hidden = false;

  const params = new URLSearchParams(location.search);
  for (const field of ["q", "category", "direction", "company"]) {
    if (params.has(field)) form.elements[field].value = params.get(field);
  }

  function apply() {
    const q = form.elements.q.value.trim().toLowerCase();
    const category = form.elements.category.value;
    const direction = form.elements.direction.value;
    const company = form.elements.company.value;
    let shown = 0;
    for (const rule of rules) {
      const d = rule.dataset;
      const match =
        (!q || q.split(/\s+/).every((word) => d.search.includes(word))) &&
        (!category || d.category === category) &&
        (!direction || d.direction === direction) &&
        (!company || d.company === company);
      rule.hidden = !match;
      if (match) shown++;
    }
    for (const group of groups) {
      group.hidden = !group.querySelector(".rule:not([hidden])");
    }
    const filtered = q || category || direction || company;
    result.textContent = filtered ? `Showing ${shown} of ${rules.length} rules` : `${rules.length} rules`;
    empty.hidden = shown > 0;

    const next = new URLSearchParams();
    for (const [key, value] of new FormData(form)) if (value) next.set(key, value);
    const query = next.toString();
    history.replaceState(null, "", (query ? `?${query}` : location.pathname) + location.hash);
  }

  form.addEventListener("input", apply);
  form.addEventListener("submit", (event) => event.preventDefault());
  apply();
})();
