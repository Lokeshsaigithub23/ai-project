let selected = [];

// Toggle Selection Card
function toggleCard(type) {

    const card = document.getElementById(type + "Card");

    if (selected.includes(type)) {

        selected = selected.filter(item => item !== type);

        card.classList.remove("border-blue-600", "bg-blue-100");

    } else {

        selected.push(type);

        card.classList.add("border-blue-600", "bg-blue-100");

    }

    buildForm();
}


// Build Dynamic Input Fields
function buildForm() {

    const container = document.getElementById("dynamicFields");

    container.innerHTML = "";

    // ---------------- TEXT ----------------

    if (selected.includes("text")) {

        container.innerHTML += `

        <div class="mb-8">

            <label class="block text-xl font-semibold mb-3">
                Topic
            </label>

            <input
                name="topic"
                id="topic"
                type="text"
                placeholder="Enter Topic"
                class="w-full border rounded-xl p-4 text-lg">

        </div>

        `;
    }

    // ---------------- IMAGE ----------------

    if (selected.includes("image")) {

        container.innerHTML += `

        <div class="mb-8">

            <label class="block text-xl font-semibold mb-3">
                Upload Image
            </label>

            <input
                name="image"
                id="image"
                type="file"
                accept="image/*"
                class="w-full border rounded-xl p-4">

        </div>

        `;
    }

    // ---------------- VIDEO ----------------

    if (selected.includes("video")) {

        container.innerHTML += `

        <div class="mb-8">

            <label class="block text-xl font-semibold mb-3">
                Upload Video
            </label>

            <input
                name="video"
                id="video"
                type="file"
                accept="video/*"
                class="w-full border rounded-xl p-4">

        </div>

        `;
    }
}


// Generate Content
function continueProcess() {

    if (selected.length === 0) {

        alert("Please select at least one option.");

        return;
    }

    // Validate Topic only if Text is selected
    if (selected.includes("text")) {

        const topic = document.getElementById("topic");

        if (!topic || topic.value.trim() === "") {

            alert("Please enter a topic.");

            return;
        }
    }

    // Validate Image
    if (selected.includes("image")) {

        const image = document.getElementById("image");

        if (!image.files.length) {

            alert("Please upload an image.");

            return;
        }
    }

    // Validate Video
    if (selected.includes("video")) {

        const video = document.getElementById("video");

        if (!video.files.length) {

            alert("Please upload a video.");

            return;
        }
    }

    // Submit Form
    document.getElementById("contentForm").submit();

}