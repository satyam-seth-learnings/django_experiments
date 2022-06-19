window.onload = () => {
    const form = document.querySelector("form");
    console.log(form);
    form.addEventListener("submit", submitForm);
    async function submitForm(event) {
        event.preventDefault();
        const formData = new FormData(form);
        console.log(formData);

        const params = new URLSearchParams();
        for (pair of formData) {
            params.append(pair[0], pair[1].toString());
        }
        console.log(params);

        try {
            const res = await fetch('/', { method: 'POST', body: params });

            if (res.status === 200) {
                form.reset()
                const data = await res.json();
                document.querySelector(".message").innerText = data.message;
            } else if (res.status === 400) {
                const data = await res.json();
                for (const error in data.errors) {
                    console.log(error);
                    console.log(data.errors[error][0].message);

                    const errorField = document.querySelector(`#id_${error}`);
                    errorField.focus();

                    errorField.parentElement.classList.add('error-field')

                    const helpSpan = document.querySelector(`#id_${error} + span.helptext`);
                    console.log(helpSpan);

                    helpSpan.innerText = data.errors[error][0].message;
                }
            }
        }
        catch (error) {
            console.log(error);
        }
    }
}
