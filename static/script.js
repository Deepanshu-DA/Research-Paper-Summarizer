document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const textarea = document.querySelector("#query");

    form.addEventListener("submit", () => {
        if (textarea.value.trim() === "") {
            alert("Please enter a research query.");
            event.preventDefault();
        }
    });
});
