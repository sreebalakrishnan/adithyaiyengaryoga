/* Progressive enhancements. All reading content remains available without JavaScript. */
const menuButton = document.querySelector(".nav-toggle");
const navigation = document.getElementById("site-nav");
function closeMenu() {
  navigation?.classList.remove("open");
  menuButton?.setAttribute("aria-expanded", "false");
  if (menuButton) menuButton.textContent = "Menu";
}
if (menuButton && navigation) {
  menuButton.addEventListener("click", () => {
    const open = navigation.classList.toggle("open");
    menuButton.setAttribute("aria-expanded", String(open));
    menuButton.textContent = open ? "Close" : "Menu";
  });
  navigation.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeMenu();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && navigation.classList.contains("open")) {
      closeMenu();
      menuButton.focus();
    }
  });
}
// Highlight the page being read in shared navigation.
for (const link of document.querySelectorAll(".site-nav a")) {
  if (new URL(link.href).pathname === location.pathname)
    link.setAttribute("aria-current", "page");
}
// Manual image selection avoids motion and keeps the caption stable while reading.
for (const gallery of document.querySelectorAll("[data-slides]")) {
  const slides = [...gallery.querySelectorAll(".slide")];
  const captions = [...gallery.querySelectorAll(".caption span")];
  const buttons = [...gallery.querySelectorAll("[data-go]")];
  buttons.forEach((button, selected) =>
    button.addEventListener("click", () => {
      slides.forEach((slide, index) => {
        slide.classList.toggle("on", index === selected);
        slide.setAttribute("aria-hidden", String(index !== selected));
      });
      captions.forEach((caption, index) => {
        caption.classList.toggle("on", index === selected);
        caption.setAttribute("aria-hidden", String(index !== selected));
      });
      buttons.forEach((item, index) =>
        item.setAttribute("aria-current", String(index === selected)),
      );
    }),
  );
  captions.forEach((caption, index) =>
    caption.setAttribute("aria-hidden", String(index !== 0)),
  );
}
for (const diagram of document.querySelectorAll("[data-inside-out]")) {
  const buttons = [...diagram.querySelectorAll("[data-set]")];
  buttons.forEach((button) =>
    button.addEventListener("click", () => {
      diagram.dataset.mode = button.dataset.set;
      buttons.forEach((item) =>
        item.setAttribute("aria-pressed", String(item === button)),
      );
    }),
  );
}
for (const building of document.querySelectorAll("[data-building]")) {
  const columns = [...building.querySelectorAll("g.col")];
  building.querySelectorAll(".limb-list li").forEach((item, index) => {
    const select = (active) =>
      columns.forEach((column, number) =>
        column.classList.toggle("on", active && number === index),
      );
    item.addEventListener("mouseenter", () => select(true));
    item.addEventListener("focus", () => select(true));
    item.addEventListener("mouseleave", () => select(false));
    item.addEventListener("blur", () => select(false));
  });
}
for (const map of document.querySelectorAll("[data-bodymap]")) {
  const areas = JSON.parse(
    map.querySelector("[data-areas]")?.textContent || "{}",
  );
  const text = map.querySelector("[data-text]");
  const buttons = [...map.querySelectorAll("[data-area]")];
  function select(area) {
    if (text && areas[area]) text.textContent = areas[area];
    buttons.forEach((button) =>
      button.setAttribute("aria-pressed", String(button.dataset.area === area)),
    );
    map
      .querySelectorAll("[data-dot]")
      .forEach((dot) => dot.classList.toggle("on", dot.dataset.dot === area));
  }
  buttons.forEach((button) =>
    button.addEventListener("click", () => select(button.dataset.area)),
  );
  if (buttons.length) select(buttons[0].dataset.area);
}
const search = document.getElementById("g-search");
const glossary = document.querySelector("[data-glossary]");
if (search && glossary) {
  const terms = [...glossary.querySelectorAll(".g-term")];
  const count = document.getElementById("g-count");
  count?.setAttribute("aria-live", "polite");
  search.addEventListener("input", () => {
    const query = search.value.trim().toLocaleLowerCase();
    let matches = 0;
    terms.forEach((term) => {
      term.hidden = !`${term.dataset.text || ""} ${term.textContent}`
        .toLocaleLowerCase()
        .includes(query);
      if (!term.hidden) matches++;
    });
    glossary.querySelectorAll(".g-group").forEach((group) => {
      group.hidden = !group.querySelector(".g-term:not([hidden])");
    });
    const empty = glossary.querySelector(".g-none");
    if (empty) empty.hidden = matches > 0;
    if (count)
      count.textContent = query
        ? `${matches} ${matches === 1 ? "term" : "terms"}`
        : "";
  });
}
