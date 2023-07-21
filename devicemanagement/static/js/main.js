let macRegex = new RegExp(/^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})|([0-9a-fA-F]{4}.[0-9a-fA-F]{4}.[0-9a-fA-F]{4})$/);
message = document.getElementById("error-message")
apiKey = document.getElementById("api-key").innerText
async function handleFormSubmit(event) {
    event.preventDefault();
    const form = event.currentTarget;
    const formData = new FormData(form);
    console.log(formData)

    if (!formData.get('mac_address') || !macRegex.test(formData.get('mac_address'))) {
        message.innerText = "Invalid Mac Address format"
        return
    }

    const plainFormData = Object.fromEntries(formData.entries());

    console.log(plainFormData)
    const body = JSON.stringify(plainFormData);

    fetchOp = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Api-Key ${apiKey}`,
            'X-CSRFToken': Cookies.get('csrftoken') // this is needed so that we can send Django's csrf token
        },
        body
    }

    const response = await fetch(form.action, fetchOp);
    if (!response.ok) {
        const errorMessage = await response.text();
        message.innerText = errorMessage;
        throw new Error(errorMessage);
    }
    else {
        message.innerText = "Device added";
    }


}
const form = document.getElementById("device-form");
form.addEventListener("submit", handleFormSubmit);