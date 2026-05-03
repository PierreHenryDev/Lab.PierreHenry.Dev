// Source tracking helper.
// If your MailerLite embed includes <input type="hidden" name="fields[source]">,
// this script fills it from ?source=... or from the form's existing book/page source.

(function () {
  const params = new URLSearchParams(window.location.search);
  const urlSource = params.get("source");

  const sourceInputs = document.querySelectorAll(
    'input[name="fields[source]"], input[name="source"], #sourceField'
  );

  sourceInputs.forEach((input) => {
    const existingSource = input.value && input.value !== "direct" ? input.value : "";
    input.value = urlSource || existingSource || "direct";
  });

  document.querySelectorAll("[data-placeholder-form]").forEach((form) => {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      alert("Replace this placeholder form with your MailerLite embedded form before publishing.");
    });
  });
})();
