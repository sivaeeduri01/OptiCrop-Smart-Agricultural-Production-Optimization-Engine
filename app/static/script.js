// ==========================
// OptiCrop AI
// script.js
// ==========================

document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    const button = document.querySelector(".predict-btn");

    if (form) {

        form.addEventListener("submit", function (e) {

            const ph = parseFloat(document.querySelector("[name='ph']").value);
            const humidity = parseFloat(document.querySelector("[name='humidity']").value);
            const temperature = parseFloat(document.querySelector("[name='temperature']").value);
            const rainfall = parseFloat(document.querySelector("[name='rainfall']").value);

            // ===== Validation =====

            if (isNaN(ph) || ph < 0 || ph > 14) {
                alert("Please enter a valid Soil pH value (0 - 14).");
                e.preventDefault();
                return;
            }

            if (isNaN(humidity) || humidity < 0 || humidity > 100) {
                alert("Humidity should be between 0% and 100%.");
                e.preventDefault();
                return;
            }

            if (isNaN(temperature) || temperature < 0 || temperature > 60) {
                alert("Please enter a valid temperature (0°C - 60°C).");
                e.preventDefault();
                return;
            }

            if (isNaN(rainfall) || rainfall < 0) {
                alert("Rainfall cannot be negative.");
                e.preventDefault();
                return;
            }

            // ===== Show Loading State =====

            if (button) {
                button.disabled = true;

                button.innerHTML = `
                    <i class="fa-solid fa-spinner fa-spin"></i>
                    Analyzing...
                `;
            }

        });

    }

    // ===== Animate Prediction Result =====

    const resultPanel = document.querySelector(".prediction-card");

    if (resultPanel) {

        resultPanel.animate(
            [
                {
                    opacity: 0,
                    transform: "translateY(30px)"
                },
                {
                    opacity: 1,
                    transform: "translateY(0px)"
                }
            ],
            {
                duration: 800,
                easing: "ease-out"
            }
        );

        resultPanel.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });

    }

});