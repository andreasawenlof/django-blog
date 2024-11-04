document.addEventListener("DOMContentLoaded", () => {
    const submitButton = document.getElementById("submitButton");
    console.log("Testing submitButton:", submitButton);

    if (submitButton) {
        submitButton.innerText = "Test Update"; // Test if this line works
    } else {
        console.error("submitButton is still null!");
    }
});