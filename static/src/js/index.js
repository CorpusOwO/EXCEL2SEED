function validateFile() {
    const input = document.getElementById("dropzone-file");
    const modal = document.getElementById("modalDialog");
    const file = input.files[0];
    const convertContainer = document.getElementById('convertContainer')

    const allowed_ext = [".xls", ".xlsx", ".csv"];
    const filename = file.name;
    const file_ext = filename.substring(filename.lastIndexOf(".")).toLowerCase();

    if (!allowed_ext.includes(file_ext)) {
        modal.classList.remove("hidden");
        input.value = "";
    } else {
        console.log(convertContainer)
        convertContainer.classList.remove("hidden");
    }
}

document.getElementById("closeDialog").addEventListener("click", function() {
    document.getElementById("modalDialog").classList.add("hidden");
});