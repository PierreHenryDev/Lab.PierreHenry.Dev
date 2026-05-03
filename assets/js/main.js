// Source tracking helper.
// Reads ?source=... from the URL and stores it in MailerLite's signup_source field.
//
// Example:
// https://lab.pierrehenry.dev?source=linkedin-fire-001
//
// MailerLite custom field required:
// signup_source

(function () {
  const params = new URLSearchParams(window.location.search);
  const urlSource = params.get("source");

  const sourceInputs = document.querySelectorAll(
    'input[name="fields[signup_source]"], input[name="fields[source]"], input[name="source"], #sourceField'
  );

  sourceInputs.forEach((input) => {
    const existingSource = input.value && input.value !== "direct" ? input.value : "";
    input.value = urlSource || existingSource || "direct";
  });
})();