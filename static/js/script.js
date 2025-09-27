function toggle_visibility(id) {
    element = document.getElementById(id)
    current = element.style.display
    if (current == "none") element.style.display = "block"
    else element.style.display = "none"
}

async function getData() {
    const url = "./svg_file_download";
    try {
        const response = await fetch(url, {
            method: "POST",
            body: JSON.stringify({
                "sequence_length": parseInt(document.getElementById("sequence_length").value),
                "image_size": parseInt(document.getElementById("image_size").value),
                "line_width": parseFloat(document.getElementById("line_width").value),
                "use_rainbow_color": document.getElementById("use_rainbow_color").checked,
                "line_color": document.getElementById("line_color").value,
                "background_color": document.getElementById("background_color").value,
                "padding": parseFloat(document.getElementById("padding").value),
                "rotate_visualization": document.getElementById("rotate_visualization").checked,
                "use_background_color": document.getElementById("use_background_color").checked,
                "saturation": parseFloat(document.getElementById("saturation").value),
                "brightness": parseFloat(document.getElementById("brightness").value),
                "alpha": parseFloat(document.getElementById("alpha").value),

            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        });
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const resp = await response.blob();
        const imgUrl = URL.createObjectURL(resp);

        const img = document.getElementById("image");
        img.src = imgUrl;
        const img_download = document.getElementById("image_download");
        img_download.href = imgUrl;
        document.getElementById("result").style.display = "block"
    } catch (error) {
        console.error(error.message);
    }
}

function switchTheme() {

    const targetTheme = document.getElementById("webPage").getAttribute('data-theme') === 'dark' ? 'light' : 'dark';

    if (targetTheme === "dark") {
        document.getElementById("light_mode_icon").style.display = "block"
        document.getElementById("dark_mode_icon").style.display = "none"

    } else {
        document.getElementById("light_mode_icon").style.display = "none"
        document.getElementById("dark_mode_icon").style.display = "block"
    }

    document.getElementById("webPage").setAttribute('data-theme', targetTheme);

    localStorage.setItem('theme', targetTheme);
}