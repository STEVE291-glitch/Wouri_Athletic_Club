// ================================
// MAIN JS - GLOBAL (SAFE)
// ================================

document.addEventListener("DOMContentLoaded", function () {
  console.log("Main.js chargé correctement ✔");

  // ================================
  // FORM VALIDATION (CONTACT, LOGIN, ETC.)
  // ================================
  const forms = document.querySelectorAll("form");

  forms.forEach((form) => {
    form.addEventListener("submit", function (e) {
      let valid = true;
      const requiredFields = form.querySelectorAll("[required]");

      requiredFields.forEach((field) => {
        if (!field.value.trim()) {
          valid = false;
          field.classList.add("input-error");
        } else {
          field.classList.remove("input-error");
        }
      });

      if (!valid) {
        e.preventDefault();
        alert("Veuillez remplir tous les champs obligatoires.");
      }
    });
  });

  // ================================
  // SMOOTH SCROLL (ANCRES)
  // ================================
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({
          behavior: "smooth",
        });
      }
    });
  });

  // ================================
  // FLASH MESSAGES AUTO-HIDE
  // ================================
  const alerts = document.querySelectorAll(".alert");

  alerts.forEach((alert) => {
    setTimeout(() => {
      alert.style.opacity = "0";
      setTimeout(() => {
        alert.remove();
      }, 500);
    }, 4000);
  });
});
